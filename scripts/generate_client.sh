#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail


# Patch generated code.
# args:
#   $1: output directory
_patch() {
    local output_dir="$1"

    echo "--- Patching generated code..."

    # Fix issue with Swagger not respecting Python subpackages
    cp -rl ${output_dir}/${PACKAGE_NAME}/* "${output_dir}/${PACKAGE_NAME//[.]/\/}/" ; rm -r ${output_dir}/${PACKAGE_NAME}

    # Prepend imports from workflow.client with argo
    find "$output_dir/${PACKAGE_NAME//[.]/\/}/" -name '*.py' -type f | while read fname; do
    {
        sed -i "s/workflows\.client/argo.workflows.client/g" $fname
    }
    done

    # Add __version__ to the client package
    echo -e "\nfrom .__about__ import __version__" \
        >> "$output_dir/${PACKAGE_NAME//[.]/\/}/__init__.py"

    echo "--- Done."
}

# Cleanup generated code.
# args:
#   $1: output directory
_cleanup() {
    local output_dir="$1"

    echo "--- Sync source files with the argo/ directory."

    local source="$(realpath $output_dir/${PACKAGE_NAME%%.*})"
    # nest the generated code under argo/ directory
    rsync \
        --link-dest="$source" \
        --recursive \
        --remove-source-files \
        --verbose \
        "$source" "$output_dir/argo/"

    echo "--- Cleanup."
    {
        set +o nounset;
        [ ! -z ${CLEANUP_DIRS} ] && rm -r ${CLEANUP_DIRS[@]}
    }

    echo "--- Done."
}

# Generates client.
# args:
#   $1: output directory
#   $2: path to openaAPI specifiaction
#   $2: path to openaAPI config
# env:
#   [required] CLIENT_VERSION   : Client version. Will be used in the comment sections of the generated code
#   [required] PACKAGE_NAME     : Name of the client package.
#   [required] KUBERNETES_BRANCH: Kubernetes branch name to get the swagger spec from
argo::generate::generate_client() {
    : "${CLIENT_VERSION?Must set CLIENT_VERSION env var}"
    : "${KUBERNETES_BRANCH?Must set KUBERNETES_BRANCH env var}"
    : "${PACKAGE_NAME?Must set PACKAGE_NAME env var}"

    echo "--- Generating client."

    local output_dir="$1"
    local openapi_spec="$2"
    local openapi_config="$3"

    mkdir -m 755 -p $output_dir
	docker run --user ${UID} --rm -v ${PWD}:/local:z swaggerapi/swagger-codegen-cli generate \
		-l python \
		-c /local/${openapi_config} \
		-i /local/${openapi_spec} \
		-o /local/${output_dir} \
        -DmodelTests=false \
		-DpackageName=${PACKAGE_NAME} \
		-DpackageVersion=${CLIENT_VERSION}

    CLEANUP_DIRS=( "${output_dir}/test" "${output_dir}/workflows/" )

    _patch   $output_dir
    _cleanup $output_dir

    echo "--- Done."
}

args=("$@")

if [ "$0" = "$BASH_SOURCE" ] ; then
    argo::generate::generate_client ${args[@]}
fi
