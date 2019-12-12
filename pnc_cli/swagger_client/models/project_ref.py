# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from datetime import datetime
from pprint import pformat
from six import iteritems
import re


class ProjectRef(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'issue_tracker_url': 'str',
        'project_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'issue_tracker_url': 'issueTrackerUrl',
        'project_url': 'projectUrl'
    }

    def __init__(self, id=None, name=None, description=None, issue_tracker_url=None, project_url=None):
        """
        ProjectRef - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._description = None
        self._issue_tracker_url = None
        self._project_url = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if issue_tracker_url is not None:
          self.issue_tracker_url = issue_tracker_url
        if project_url is not None:
          self.project_url = project_url

    @property
    def id(self):
        """
        Gets the id of this ProjectRef.

        :return: The id of this ProjectRef.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProjectRef.

        :param id: The id of this ProjectRef.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ProjectRef.

        :return: The name of this ProjectRef.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProjectRef.

        :param name: The name of this ProjectRef.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ProjectRef.

        :return: The description of this ProjectRef.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProjectRef.

        :param description: The description of this ProjectRef.
        :type: str
        """

        self._description = description

    @property
    def issue_tracker_url(self):
        """
        Gets the issue_tracker_url of this ProjectRef.

        :return: The issue_tracker_url of this ProjectRef.
        :rtype: str
        """
        return self._issue_tracker_url

    @issue_tracker_url.setter
    def issue_tracker_url(self, issue_tracker_url):
        """
        Sets the issue_tracker_url of this ProjectRef.

        :param issue_tracker_url: The issue_tracker_url of this ProjectRef.
        :type: str
        """

        self._issue_tracker_url = issue_tracker_url

    @property
    def project_url(self):
        """
        Gets the project_url of this ProjectRef.

        :return: The project_url of this ProjectRef.
        :rtype: str
        """
        return self._project_url

    @project_url.setter
    def project_url(self, project_url):
        """
        Sets the project_url of this ProjectRef.

        :param project_url: The project_url of this ProjectRef.
        :type: str
        """

        self._project_url = project_url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
            elif isinstance(value, datetime):
                result[attr] = str(value.date())
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ProjectRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other