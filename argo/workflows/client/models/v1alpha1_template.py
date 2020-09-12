# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    The version of the OpenAPI document: 2.10.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.workflows.client.configuration import Configuration


class V1alpha1Template(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'active_deadline_seconds': 'int',
        'affinity': 'V1Affinity',
        'archive_location': 'V1alpha1ArtifactLocation',
        'arguments': 'V1alpha1Arguments',
        'automount_service_account_token': 'bool',
        'container': 'V1Container',
        'daemon': 'bool',
        'dag': 'V1alpha1DAGTemplate',
        'executor': 'V1alpha1ExecutorConfig',
        'host_aliases': 'list[V1HostAlias]',
        'init_containers': 'list[V1alpha1UserContainer]',
        'inputs': 'V1alpha1Inputs',
        'metadata': 'V1alpha1Metadata',
        'metrics': 'V1alpha1Metrics',
        'name': 'str',
        'node_selector': 'dict(str, str)',
        'outputs': 'V1alpha1Outputs',
        'parallelism': 'int',
        'pod_spec_patch': 'str',
        'priority': 'int',
        'priority_class_name': 'str',
        'resource': 'V1alpha1ResourceTemplate',
        'resubmit_pending_pods': 'bool',
        'retry_strategy': 'V1alpha1RetryStrategy',
        'scheduler_name': 'str',
        'script': 'V1alpha1ScriptTemplate',
        'security_context': 'V1PodSecurityContext',
        'service_account_name': 'str',
        'sidecars': 'list[V1alpha1UserContainer]',
        'steps': 'list[list[V1alpha1WorkflowStep]]',
        'suspend': 'V1alpha1SuspendTemplate',
        'synchronization': 'V1alpha1Synchronization',
        'template': 'str',
        'template_ref': 'V1alpha1TemplateRef',
        'tolerations': 'list[V1Toleration]',
        'volumes': 'list[V1Volume]'
    }

    attribute_map = {
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'affinity': 'affinity',
        'archive_location': 'archiveLocation',
        'arguments': 'arguments',
        'automount_service_account_token': 'automountServiceAccountToken',
        'container': 'container',
        'daemon': 'daemon',
        'dag': 'dag',
        'executor': 'executor',
        'host_aliases': 'hostAliases',
        'init_containers': 'initContainers',
        'inputs': 'inputs',
        'metadata': 'metadata',
        'metrics': 'metrics',
        'name': 'name',
        'node_selector': 'nodeSelector',
        'outputs': 'outputs',
        'parallelism': 'parallelism',
        'pod_spec_patch': 'podSpecPatch',
        'priority': 'priority',
        'priority_class_name': 'priorityClassName',
        'resource': 'resource',
        'resubmit_pending_pods': 'resubmitPendingPods',
        'retry_strategy': 'retryStrategy',
        'scheduler_name': 'schedulerName',
        'script': 'script',
        'security_context': 'securityContext',
        'service_account_name': 'serviceAccountName',
        'sidecars': 'sidecars',
        'steps': 'steps',
        'suspend': 'suspend',
        'synchronization': 'synchronization',
        'template': 'template',
        'template_ref': 'templateRef',
        'tolerations': 'tolerations',
        'volumes': 'volumes'
    }

    def __init__(self, active_deadline_seconds=None, affinity=None, archive_location=None, arguments=None, automount_service_account_token=None, container=None, daemon=None, dag=None, executor=None, host_aliases=None, init_containers=None, inputs=None, metadata=None, metrics=None, name=None, node_selector=None, outputs=None, parallelism=None, pod_spec_patch=None, priority=None, priority_class_name=None, resource=None, resubmit_pending_pods=None, retry_strategy=None, scheduler_name=None, script=None, security_context=None, service_account_name=None, sidecars=None, steps=None, suspend=None, synchronization=None, template=None, template_ref=None, tolerations=None, volumes=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1Template - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active_deadline_seconds = None
        self._affinity = None
        self._archive_location = None
        self._arguments = None
        self._automount_service_account_token = None
        self._container = None
        self._daemon = None
        self._dag = None
        self._executor = None
        self._host_aliases = None
        self._init_containers = None
        self._inputs = None
        self._metadata = None
        self._metrics = None
        self._name = None
        self._node_selector = None
        self._outputs = None
        self._parallelism = None
        self._pod_spec_patch = None
        self._priority = None
        self._priority_class_name = None
        self._resource = None
        self._resubmit_pending_pods = None
        self._retry_strategy = None
        self._scheduler_name = None
        self._script = None
        self._security_context = None
        self._service_account_name = None
        self._sidecars = None
        self._steps = None
        self._suspend = None
        self._synchronization = None
        self._template = None
        self._template_ref = None
        self._tolerations = None
        self._volumes = None
        self.discriminator = None

        if active_deadline_seconds is not None:
            self.active_deadline_seconds = active_deadline_seconds
        if affinity is not None:
            self.affinity = affinity
        if archive_location is not None:
            self.archive_location = archive_location
        if arguments is not None:
            self.arguments = arguments
        if automount_service_account_token is not None:
            self.automount_service_account_token = automount_service_account_token
        if container is not None:
            self.container = container
        if daemon is not None:
            self.daemon = daemon
        if dag is not None:
            self.dag = dag
        if executor is not None:
            self.executor = executor
        if host_aliases is not None:
            self.host_aliases = host_aliases
        if init_containers is not None:
            self.init_containers = init_containers
        if inputs is not None:
            self.inputs = inputs
        if metadata is not None:
            self.metadata = metadata
        if metrics is not None:
            self.metrics = metrics
        self.name = name
        if node_selector is not None:
            self.node_selector = node_selector
        if outputs is not None:
            self.outputs = outputs
        if parallelism is not None:
            self.parallelism = parallelism
        if pod_spec_patch is not None:
            self.pod_spec_patch = pod_spec_patch
        if priority is not None:
            self.priority = priority
        if priority_class_name is not None:
            self.priority_class_name = priority_class_name
        if resource is not None:
            self.resource = resource
        if resubmit_pending_pods is not None:
            self.resubmit_pending_pods = resubmit_pending_pods
        if retry_strategy is not None:
            self.retry_strategy = retry_strategy
        if scheduler_name is not None:
            self.scheduler_name = scheduler_name
        if script is not None:
            self.script = script
        if security_context is not None:
            self.security_context = security_context
        if service_account_name is not None:
            self.service_account_name = service_account_name
        if sidecars is not None:
            self.sidecars = sidecars
        if steps is not None:
            self.steps = steps
        if suspend is not None:
            self.suspend = suspend
        if synchronization is not None:
            self.synchronization = synchronization
        if template is not None:
            self.template = template
        if template_ref is not None:
            self.template_ref = template_ref
        if tolerations is not None:
            self.tolerations = tolerations
        if volumes is not None:
            self.volumes = volumes

    @property
    def active_deadline_seconds(self):
        """Gets the active_deadline_seconds of this V1alpha1Template.  # noqa: E501

        Optional duration in seconds relative to the StartTime that the pod may be active on a node before the system actively tries to terminate the pod; value must be positive integer This field is only applicable to container and script templates.  # noqa: E501

        :return: The active_deadline_seconds of this V1alpha1Template.  # noqa: E501
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """Sets the active_deadline_seconds of this V1alpha1Template.

        Optional duration in seconds relative to the StartTime that the pod may be active on a node before the system actively tries to terminate the pod; value must be positive integer This field is only applicable to container and script templates.  # noqa: E501

        :param active_deadline_seconds: The active_deadline_seconds of this V1alpha1Template.  # noqa: E501
        :type: int
        """

        self._active_deadline_seconds = active_deadline_seconds

    @property
    def affinity(self):
        """Gets the affinity of this V1alpha1Template.  # noqa: E501


        :return: The affinity of this V1alpha1Template.  # noqa: E501
        :rtype: V1Affinity
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this V1alpha1Template.


        :param affinity: The affinity of this V1alpha1Template.  # noqa: E501
        :type: V1Affinity
        """

        self._affinity = affinity

    @property
    def archive_location(self):
        """Gets the archive_location of this V1alpha1Template.  # noqa: E501


        :return: The archive_location of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1ArtifactLocation
        """
        return self._archive_location

    @archive_location.setter
    def archive_location(self, archive_location):
        """Sets the archive_location of this V1alpha1Template.


        :param archive_location: The archive_location of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1ArtifactLocation
        """

        self._archive_location = archive_location

    @property
    def arguments(self):
        """Gets the arguments of this V1alpha1Template.  # noqa: E501


        :return: The arguments of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1Arguments
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this V1alpha1Template.


        :param arguments: The arguments of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1Arguments
        """

        self._arguments = arguments

    @property
    def automount_service_account_token(self):
        """Gets the automount_service_account_token of this V1alpha1Template.  # noqa: E501

        AutomountServiceAccountToken indicates whether a service account token should be automatically mounted in pods. ServiceAccountName of ExecutorConfig must be specified if this value is false.  # noqa: E501

        :return: The automount_service_account_token of this V1alpha1Template.  # noqa: E501
        :rtype: bool
        """
        return self._automount_service_account_token

    @automount_service_account_token.setter
    def automount_service_account_token(self, automount_service_account_token):
        """Sets the automount_service_account_token of this V1alpha1Template.

        AutomountServiceAccountToken indicates whether a service account token should be automatically mounted in pods. ServiceAccountName of ExecutorConfig must be specified if this value is false.  # noqa: E501

        :param automount_service_account_token: The automount_service_account_token of this V1alpha1Template.  # noqa: E501
        :type: bool
        """

        self._automount_service_account_token = automount_service_account_token

    @property
    def container(self):
        """Gets the container of this V1alpha1Template.  # noqa: E501


        :return: The container of this V1alpha1Template.  # noqa: E501
        :rtype: V1Container
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this V1alpha1Template.


        :param container: The container of this V1alpha1Template.  # noqa: E501
        :type: V1Container
        """

        self._container = container

    @property
    def daemon(self):
        """Gets the daemon of this V1alpha1Template.  # noqa: E501

        Deamon will allow a workflow to proceed to the next step so long as the container reaches readiness  # noqa: E501

        :return: The daemon of this V1alpha1Template.  # noqa: E501
        :rtype: bool
        """
        return self._daemon

    @daemon.setter
    def daemon(self, daemon):
        """Sets the daemon of this V1alpha1Template.

        Deamon will allow a workflow to proceed to the next step so long as the container reaches readiness  # noqa: E501

        :param daemon: The daemon of this V1alpha1Template.  # noqa: E501
        :type: bool
        """

        self._daemon = daemon

    @property
    def dag(self):
        """Gets the dag of this V1alpha1Template.  # noqa: E501


        :return: The dag of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1DAGTemplate
        """
        return self._dag

    @dag.setter
    def dag(self, dag):
        """Sets the dag of this V1alpha1Template.


        :param dag: The dag of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1DAGTemplate
        """

        self._dag = dag

    @property
    def executor(self):
        """Gets the executor of this V1alpha1Template.  # noqa: E501


        :return: The executor of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1ExecutorConfig
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        """Sets the executor of this V1alpha1Template.


        :param executor: The executor of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1ExecutorConfig
        """

        self._executor = executor

    @property
    def host_aliases(self):
        """Gets the host_aliases of this V1alpha1Template.  # noqa: E501

        HostAliases is an optional list of hosts and IPs that will be injected into the pod spec  # noqa: E501

        :return: The host_aliases of this V1alpha1Template.  # noqa: E501
        :rtype: list[V1HostAlias]
        """
        return self._host_aliases

    @host_aliases.setter
    def host_aliases(self, host_aliases):
        """Sets the host_aliases of this V1alpha1Template.

        HostAliases is an optional list of hosts and IPs that will be injected into the pod spec  # noqa: E501

        :param host_aliases: The host_aliases of this V1alpha1Template.  # noqa: E501
        :type: list[V1HostAlias]
        """

        self._host_aliases = host_aliases

    @property
    def init_containers(self):
        """Gets the init_containers of this V1alpha1Template.  # noqa: E501

        InitContainers is a list of containers which run before the main container.  # noqa: E501

        :return: The init_containers of this V1alpha1Template.  # noqa: E501
        :rtype: list[V1alpha1UserContainer]
        """
        return self._init_containers

    @init_containers.setter
    def init_containers(self, init_containers):
        """Sets the init_containers of this V1alpha1Template.

        InitContainers is a list of containers which run before the main container.  # noqa: E501

        :param init_containers: The init_containers of this V1alpha1Template.  # noqa: E501
        :type: list[V1alpha1UserContainer]
        """

        self._init_containers = init_containers

    @property
    def inputs(self):
        """Gets the inputs of this V1alpha1Template.  # noqa: E501


        :return: The inputs of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1Inputs
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this V1alpha1Template.


        :param inputs: The inputs of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1Inputs
        """

        self._inputs = inputs

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1Template.  # noqa: E501


        :return: The metadata of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1Template.


        :param metadata: The metadata of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1Metadata
        """

        self._metadata = metadata

    @property
    def metrics(self):
        """Gets the metrics of this V1alpha1Template.  # noqa: E501


        :return: The metrics of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1Metrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this V1alpha1Template.


        :param metrics: The metrics of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1Metrics
        """

        self._metrics = metrics

    @property
    def name(self):
        """Gets the name of this V1alpha1Template.  # noqa: E501

        Name is the name of the template  # noqa: E501

        :return: The name of this V1alpha1Template.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1Template.

        Name is the name of the template  # noqa: E501

        :param name: The name of this V1alpha1Template.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def node_selector(self):
        """Gets the node_selector of this V1alpha1Template.  # noqa: E501

        NodeSelector is a selector to schedule this step of the workflow to be run on the selected node(s). Overrides the selector set at the workflow level.  # noqa: E501

        :return: The node_selector of this V1alpha1Template.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this V1alpha1Template.

        NodeSelector is a selector to schedule this step of the workflow to be run on the selected node(s). Overrides the selector set at the workflow level.  # noqa: E501

        :param node_selector: The node_selector of this V1alpha1Template.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def outputs(self):
        """Gets the outputs of this V1alpha1Template.  # noqa: E501


        :return: The outputs of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1Outputs
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this V1alpha1Template.


        :param outputs: The outputs of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1Outputs
        """

        self._outputs = outputs

    @property
    def parallelism(self):
        """Gets the parallelism of this V1alpha1Template.  # noqa: E501

        Parallelism limits the max total parallel pods that can execute at the same time within the boundaries of this template invocation. If additional steps/dag templates are invoked, the pods created by those templates will not be counted towards this total.  # noqa: E501

        :return: The parallelism of this V1alpha1Template.  # noqa: E501
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this V1alpha1Template.

        Parallelism limits the max total parallel pods that can execute at the same time within the boundaries of this template invocation. If additional steps/dag templates are invoked, the pods created by those templates will not be counted towards this total.  # noqa: E501

        :param parallelism: The parallelism of this V1alpha1Template.  # noqa: E501
        :type: int
        """

        self._parallelism = parallelism

    @property
    def pod_spec_patch(self):
        """Gets the pod_spec_patch of this V1alpha1Template.  # noqa: E501

        PodSpecPatch holds strategic merge patch to apply against the pod spec. Allows parameterization of container fields which are not strings (e.g. resource limits).  # noqa: E501

        :return: The pod_spec_patch of this V1alpha1Template.  # noqa: E501
        :rtype: str
        """
        return self._pod_spec_patch

    @pod_spec_patch.setter
    def pod_spec_patch(self, pod_spec_patch):
        """Sets the pod_spec_patch of this V1alpha1Template.

        PodSpecPatch holds strategic merge patch to apply against the pod spec. Allows parameterization of container fields which are not strings (e.g. resource limits).  # noqa: E501

        :param pod_spec_patch: The pod_spec_patch of this V1alpha1Template.  # noqa: E501
        :type: str
        """

        self._pod_spec_patch = pod_spec_patch

    @property
    def priority(self):
        """Gets the priority of this V1alpha1Template.  # noqa: E501

        Priority to apply to workflow pods.  # noqa: E501

        :return: The priority of this V1alpha1Template.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this V1alpha1Template.

        Priority to apply to workflow pods.  # noqa: E501

        :param priority: The priority of this V1alpha1Template.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def priority_class_name(self):
        """Gets the priority_class_name of this V1alpha1Template.  # noqa: E501

        PriorityClassName to apply to workflow pods.  # noqa: E501

        :return: The priority_class_name of this V1alpha1Template.  # noqa: E501
        :rtype: str
        """
        return self._priority_class_name

    @priority_class_name.setter
    def priority_class_name(self, priority_class_name):
        """Sets the priority_class_name of this V1alpha1Template.

        PriorityClassName to apply to workflow pods.  # noqa: E501

        :param priority_class_name: The priority_class_name of this V1alpha1Template.  # noqa: E501
        :type: str
        """

        self._priority_class_name = priority_class_name

    @property
    def resource(self):
        """Gets the resource of this V1alpha1Template.  # noqa: E501


        :return: The resource of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1ResourceTemplate
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this V1alpha1Template.


        :param resource: The resource of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1ResourceTemplate
        """

        self._resource = resource

    @property
    def resubmit_pending_pods(self):
        """Gets the resubmit_pending_pods of this V1alpha1Template.  # noqa: E501

        ResubmitPendingPods is a flag to enable resubmitting pods that remain Pending after initial submission  # noqa: E501

        :return: The resubmit_pending_pods of this V1alpha1Template.  # noqa: E501
        :rtype: bool
        """
        return self._resubmit_pending_pods

    @resubmit_pending_pods.setter
    def resubmit_pending_pods(self, resubmit_pending_pods):
        """Sets the resubmit_pending_pods of this V1alpha1Template.

        ResubmitPendingPods is a flag to enable resubmitting pods that remain Pending after initial submission  # noqa: E501

        :param resubmit_pending_pods: The resubmit_pending_pods of this V1alpha1Template.  # noqa: E501
        :type: bool
        """

        self._resubmit_pending_pods = resubmit_pending_pods

    @property
    def retry_strategy(self):
        """Gets the retry_strategy of this V1alpha1Template.  # noqa: E501


        :return: The retry_strategy of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1RetryStrategy
        """
        return self._retry_strategy

    @retry_strategy.setter
    def retry_strategy(self, retry_strategy):
        """Sets the retry_strategy of this V1alpha1Template.


        :param retry_strategy: The retry_strategy of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1RetryStrategy
        """

        self._retry_strategy = retry_strategy

    @property
    def scheduler_name(self):
        """Gets the scheduler_name of this V1alpha1Template.  # noqa: E501

        If specified, the pod will be dispatched by specified scheduler. Or it will be dispatched by workflow scope scheduler if specified. If neither specified, the pod will be dispatched by default scheduler.  # noqa: E501

        :return: The scheduler_name of this V1alpha1Template.  # noqa: E501
        :rtype: str
        """
        return self._scheduler_name

    @scheduler_name.setter
    def scheduler_name(self, scheduler_name):
        """Sets the scheduler_name of this V1alpha1Template.

        If specified, the pod will be dispatched by specified scheduler. Or it will be dispatched by workflow scope scheduler if specified. If neither specified, the pod will be dispatched by default scheduler.  # noqa: E501

        :param scheduler_name: The scheduler_name of this V1alpha1Template.  # noqa: E501
        :type: str
        """

        self._scheduler_name = scheduler_name

    @property
    def script(self):
        """Gets the script of this V1alpha1Template.  # noqa: E501


        :return: The script of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1ScriptTemplate
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this V1alpha1Template.


        :param script: The script of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1ScriptTemplate
        """

        self._script = script

    @property
    def security_context(self):
        """Gets the security_context of this V1alpha1Template.  # noqa: E501


        :return: The security_context of this V1alpha1Template.  # noqa: E501
        :rtype: V1PodSecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """Sets the security_context of this V1alpha1Template.


        :param security_context: The security_context of this V1alpha1Template.  # noqa: E501
        :type: V1PodSecurityContext
        """

        self._security_context = security_context

    @property
    def service_account_name(self):
        """Gets the service_account_name of this V1alpha1Template.  # noqa: E501

        ServiceAccountName to apply to workflow pods  # noqa: E501

        :return: The service_account_name of this V1alpha1Template.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this V1alpha1Template.

        ServiceAccountName to apply to workflow pods  # noqa: E501

        :param service_account_name: The service_account_name of this V1alpha1Template.  # noqa: E501
        :type: str
        """

        self._service_account_name = service_account_name

    @property
    def sidecars(self):
        """Gets the sidecars of this V1alpha1Template.  # noqa: E501

        Sidecars is a list of containers which run alongside the main container Sidecars are automatically killed when the main container completes  # noqa: E501

        :return: The sidecars of this V1alpha1Template.  # noqa: E501
        :rtype: list[V1alpha1UserContainer]
        """
        return self._sidecars

    @sidecars.setter
    def sidecars(self, sidecars):
        """Sets the sidecars of this V1alpha1Template.

        Sidecars is a list of containers which run alongside the main container Sidecars are automatically killed when the main container completes  # noqa: E501

        :param sidecars: The sidecars of this V1alpha1Template.  # noqa: E501
        :type: list[V1alpha1UserContainer]
        """

        self._sidecars = sidecars

    @property
    def steps(self):
        """Gets the steps of this V1alpha1Template.  # noqa: E501

        Steps define a series of sequential/parallel workflow steps  # noqa: E501

        :return: The steps of this V1alpha1Template.  # noqa: E501
        :rtype: list[list[V1alpha1WorkflowStep]]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this V1alpha1Template.

        Steps define a series of sequential/parallel workflow steps  # noqa: E501

        :param steps: The steps of this V1alpha1Template.  # noqa: E501
        :type: list[list[V1alpha1WorkflowStep]]
        """

        self._steps = steps

    @property
    def suspend(self):
        """Gets the suspend of this V1alpha1Template.  # noqa: E501


        :return: The suspend of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1SuspendTemplate
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """Sets the suspend of this V1alpha1Template.


        :param suspend: The suspend of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1SuspendTemplate
        """

        self._suspend = suspend

    @property
    def synchronization(self):
        """Gets the synchronization of this V1alpha1Template.  # noqa: E501


        :return: The synchronization of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1Synchronization
        """
        return self._synchronization

    @synchronization.setter
    def synchronization(self, synchronization):
        """Sets the synchronization of this V1alpha1Template.


        :param synchronization: The synchronization of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1Synchronization
        """

        self._synchronization = synchronization

    @property
    def template(self):
        """Gets the template of this V1alpha1Template.  # noqa: E501

        Template is the name of the template which is used as the base of this template. DEPRECATED: This field is not used.  # noqa: E501

        :return: The template of this V1alpha1Template.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1alpha1Template.

        Template is the name of the template which is used as the base of this template. DEPRECATED: This field is not used.  # noqa: E501

        :param template: The template of this V1alpha1Template.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def template_ref(self):
        """Gets the template_ref of this V1alpha1Template.  # noqa: E501


        :return: The template_ref of this V1alpha1Template.  # noqa: E501
        :rtype: V1alpha1TemplateRef
        """
        return self._template_ref

    @template_ref.setter
    def template_ref(self, template_ref):
        """Sets the template_ref of this V1alpha1Template.


        :param template_ref: The template_ref of this V1alpha1Template.  # noqa: E501
        :type: V1alpha1TemplateRef
        """

        self._template_ref = template_ref

    @property
    def tolerations(self):
        """Gets the tolerations of this V1alpha1Template.  # noqa: E501

        Tolerations to apply to workflow pods.  # noqa: E501

        :return: The tolerations of this V1alpha1Template.  # noqa: E501
        :rtype: list[V1Toleration]
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """Sets the tolerations of this V1alpha1Template.

        Tolerations to apply to workflow pods.  # noqa: E501

        :param tolerations: The tolerations of this V1alpha1Template.  # noqa: E501
        :type: list[V1Toleration]
        """

        self._tolerations = tolerations

    @property
    def volumes(self):
        """Gets the volumes of this V1alpha1Template.  # noqa: E501

        Volumes is a list of volumes that can be mounted by containers in a template.  # noqa: E501

        :return: The volumes of this V1alpha1Template.  # noqa: E501
        :rtype: list[V1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this V1alpha1Template.

        Volumes is a list of volumes that can be mounted by containers in a template.  # noqa: E501

        :param volumes: The volumes of this V1alpha1Template.  # noqa: E501
        :type: list[V1Volume]
        """

        self._volumes = volumes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1Template):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1Template):
            return True

        return self.to_dict() != other.to_dict()
