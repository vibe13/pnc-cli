from argh import arg
import client
from client.BuildconfigurationsApi import BuildconfigurationsApi
import utils

__author__ = 'thauser'
def _create_build_configuration(name, project_id, environment, description, scm_url, scm_revision, patches_url,
                                build_script):
    created_build_configuration = client.models.Configuration.Configuration()
    created_build_configuration.name = name
    created_build_configuration.projectId = project_id
    return created_build_configuration

def _get_build_configuration_id_by_name(name):
    """
    Returns the id of the build configuration matching name
    :param name: name of build configuration
    :return: id of the matching build configuration, or None if no match found
    """
    response = BuildconfigurationsApi(utils.get_api_client()).getAll()
    for config in response.json():
        if config["name"] == name:
            return config["id"]
    return None

def _build_configuration_exists(search_id):
    """
    Test if a build configuration matching search_id exists
    :param search_id: id to test for
    :return: True if a build configuration with search_id exists
    """
    response = BuildconfigurationsApi(utils.get_api_client()).getSpecific(id=search_id)
    if response.ok:
        return True
    return False

@arg("-n", "--name", help="Name of the build configuration to trigger")
@arg("-i", "--id", help="ID of the build configuration to trigger")
def build(name=None,id=None):
    """Trigger a build configuration giving either the name or ID."""
    if id:
        if _build_configuration_exists(id):
            print(utils.pretty_format_response(BuildconfigurationsApi(utils.get_api_client()).trigger(id=id).json()))
        else:
            print("There is no build configuration with id {0}.".format(id))
    elif name:
        id = _get_build_configuration_id_by_name(name)
        if id:
            print(utils.pretty_format_response(BuildconfigurationsApi(utils.get_api_client()).trigger(id=id).json()))
        else:
            print("There is no build configuration with name {0}.".format(name))
    else:
        print("Build requires either a name or an ID of a build configuration to trigger.")


def create_build_configuration(name, project_id, environment, description="", scm_url="", scm_revision="", patches_url="",
                               build_script=""):
    #check for existing project_ids, fail out if the project id doesn't exist
    build_configuration = _create_build_configuration(name, project_id, environment, description, scm_url, scm_revision, patches_url, build_script)
    response = utils.pretty_format_response(BuildconfigurationsApi(utils.get_api_client()).createNew(body=build_configuration).json())
    print(response)


@arg("-a", "--attributes", help="List of attributes to retrieve. Will print given attributes separated by whitespace.")
def list_build_configurations(attributes=None):
    response = BuildconfigurationsApi(utils.get_api_client()).getAll()

    if attributes is not None:
        attr_list = attributes.split(",")
        for a in attr_list:
            if a not in client.models.Configuration.Configuration().attributeMap:
                print('Please choose attribute(s) from the following list:')
                print('\n'.join(key for key in client.models.Configuration.Configuration().attributeMap))
                return
        result = utils.retrieve_keys(response.json(), attr_list)
        print('\n'.join(str(r[attr]) for r in result for attr in attr_list))
    else:
        build_configurations = response.json()
        for bc in build_configurations:
            print('-------------------------')
            print ('\n'.join(key + ": " +str(bc[key])  for key in bc.keys()))
            print('-------------------------')
