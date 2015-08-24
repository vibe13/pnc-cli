#!/usr/bin/env python
"""
BuildrecordsApi.py
Copyright 2015 Reverb Technologies, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os
import urllib

from models import *


class BuildrecordsApi(object):

    def __init__(self, api_client):
      self.api_client = api_client

    
    def getAll(self, **kwargs):
        """Gets all Build Records

        Args:
            
            pageIndex, int: Page index (required)
            
            pageSize, int: Pagination size (required)
            
            sort, str: Sorting RSQL (required)
            
            q, str: RSQL query (required)
            
        Returns: list[BuildRecord]
        """

        all_params = ['pageIndex', 'pageSize', 'sort', 'q']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAll" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/build-records'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        query_params = {}
        header_params = {}
        form_params = {}
        files = {}
        body_param = None

        
        if 'pageIndex' in params:
            query_params['pageIndex'] = self.api_client.to_path_value(params['pageIndex'])
        
        if 'pageSize' in params:
            query_params['pageSize'] = self.api_client.to_path_value(params['pageSize'])
        
        if 'sort' in params:
            query_params['sort'] = self.api_client.to_path_value(params['sort'])
        
        if 'q' in params:
            query_params['q'] = self.api_client.to_path_value(params['q'])
        

        

        

        

        

        post_data = (form_params if form_params else body_param)

        response = self.api_client.callAPI(resource_path, method, query_params,
                                          post_data, header_params, files=files)
        return response

   
    def getAllForBuildConfiguration(self, **kwargs):
        """Gets the Build Records linked to a specific Build Configuration

        Args:
            
            pageIndex, int: Page index (required)
            
            pageSize, int: Pagination size (required)
            
            sort, str: Sorting RSQL (required)
            
            q, str: RSQL query (required)
            
            configurationId, int: Build Configuration id (required)
            
        Returns: list[BuildRecord]
        """

        all_params = ['pageIndex', 'pageSize', 'sort', 'q', 'configurationId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllForBuildConfiguration" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/build-records/build-configurations/{configurationId}'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        query_params = {}
        header_params = {}
        form_params = {}
        files = {}
        body_param = None

        
        if 'pageIndex' in params:
            query_params['pageIndex'] = self.api_client.to_path_value(params['pageIndex'])
        
        if 'pageSize' in params:
            query_params['pageSize'] = self.api_client.to_path_value(params['pageSize'])
        
        if 'sort' in params:
            query_params['sort'] = self.api_client.to_path_value(params['sort'])
        
        if 'q' in params:
            query_params['q'] = self.api_client.to_path_value(params['q'])
        

        

        
        if 'configurationId' in params:
            replacement = str(self.api_client.to_path_value(params['configurationId']))
            replacement = urllib.quote(replacement)
            resource_path = resource_path.replace('{' + 'configurationId' + '}',
                                                replacement)
        

        

        

        post_data = (form_params if form_params else body_param)

        response = self.api_client.callAPI(resource_path, method, query_params,
                                          post_data, header_params, files=files)
        return response

   
    def getAllForProject(self, **kwargs):
        """Gets the Build Records linked to a specific Project

        Args:
            
            pageIndex, int: Page index (required)
            
            pageSize, int: Pagination size (required)
            
            sort, str: Sorting RSQL (required)
            
            projectId, int: Project id (required)
            
            q, str: RSQL query (required)
            
        Returns: list[BuildRecord]
        """

        all_params = ['pageIndex', 'pageSize', 'sort', 'projectId', 'q']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllForProject" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/build-records/projects/{projectId}'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        query_params = {}
        header_params = {}
        form_params = {}
        files = {}
        body_param = None

        
        if 'pageIndex' in params:
            query_params['pageIndex'] = self.api_client.to_path_value(params['pageIndex'])
        
        if 'pageSize' in params:
            query_params['pageSize'] = self.api_client.to_path_value(params['pageSize'])
        
        if 'sort' in params:
            query_params['sort'] = self.api_client.to_path_value(params['sort'])
        
        if 'q' in params:
            query_params['q'] = self.api_client.to_path_value(params['q'])
        

        

        
        if 'projectId' in params:
            replacement = str(self.api_client.to_path_value(params['projectId']))
            replacement = urllib.quote(replacement)
            resource_path = resource_path.replace('{' + 'projectId' + '}',
                                                replacement)
        

        

        

        post_data = (form_params if form_params else body_param)

        response = self.api_client.callAPI(resource_path, method, query_params,
                                          post_data, header_params, files=files)
        return response

   
    def getSpecific(self, **kwargs):
        """Gets specific Build Record

        Args:
            
            id, int: BuildRecord id (required)
            
        Returns: BuildRecord
        """

        all_params = ['id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSpecific" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/build-records/{id}'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        query_params = {}
        header_params = {}
        form_params = {}
        files = {}
        body_param = None

        

        

        
        if 'id' in params:
            replacement = str(self.api_client.to_path_value(params['id']))
            replacement = urllib.quote(replacement)
            resource_path = resource_path.replace('{' + 'id' + '}',
                                                replacement)
        

        

        

        post_data = (form_params if form_params else body_param)

        response = self.api_client.callAPI(resource_path, method, query_params,
                                          post_data, header_params, files=files)
        return response

   
    def getArtifacts(self, **kwargs):
        """Gets artifacts for specific Build Record

        Args:
            
            id, int: BuildRecord id (required)
            
            pageIndex, int: Page index (required)
            
            pageSize, int: Pagination size (required)
            
            sort, str: Sorting RSQL (required)
            
            q, str: RSQL query (required)
            
        Returns: list[Artifact]
        """

        all_params = ['id', 'pageIndex', 'pageSize', 'sort', 'q']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method getArtifacts" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/build-records/{id}/artifacts'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        query_params = {}
        header_params = {}
        form_params = {}
        files = {}
        body_param = None

        
        if 'pageIndex' in params:
            query_params['pageIndex'] = self.api_client.to_path_value(params['pageIndex'])
        
        if 'pageSize' in params:
            query_params['pageSize'] = self.api_client.to_path_value(params['pageSize'])
        
        if 'sort' in params:
            query_params['sort'] = self.api_client.to_path_value(params['sort'])
        
        if 'q' in params:
            query_params['q'] = self.api_client.to_path_value(params['q'])
        

        

        
        if 'id' in params:
            replacement = str(self.api_client.to_path_value(params['id']))
            replacement = urllib.quote(replacement)
            resource_path = resource_path.replace('{' + 'id' + '}',
                                                replacement)
        

        

        

        post_data = (form_params if form_params else body_param)

        response = self.api_client.callAPI(resource_path, method, query_params,
                                          post_data, header_params, files=files)
        return response

   
    def getBuildConfigurationAudited(self, **kwargs):
        """Gets the audited build configuration for specific build record

        Args:
            
            id, int: BuildRecord id (required)
            
        Returns: BuildConfigurationAudited
        """

        all_params = ['id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method getBuildConfigurationAudited" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/build-records/{id}/build-configuration-audited'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        query_params = {}
        header_params = {}
        form_params = {}
        files = {}
        body_param = None

        

        

        
        if 'id' in params:
            replacement = str(self.api_client.to_path_value(params['id']))
            replacement = urllib.quote(replacement)
            resource_path = resource_path.replace('{' + 'id' + '}',
                                                replacement)
        

        

        

        post_data = (form_params if form_params else body_param)

        response = self.api_client.callAPI(resource_path, method, query_params,
                                          post_data, header_params, files=files)
        return response

   
    def getLogs(self, **kwargs):
        """Gets logs for specific Build Record

        Args:
            
            id, int: BuildRecord id (required)
            
        Returns: str
        """

        all_params = ['id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLogs" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/build-records/{id}/log'
        resource_path = resource_path.replace('{format}', 'json')
        method = 'GET'

        query_params = {}
        header_params = {}
        form_params = {}
        files = {}
        body_param = None

        

        

        
        if 'id' in params:
            replacement = str(self.api_client.to_path_value(params['id']))
            replacement = urllib.quote(replacement)
            resource_path = resource_path.replace('{' + 'id' + '}',
                                                replacement)
        

        

        

        post_data = (form_params if form_params else body_param)

        response = self.api_client.callAPI(resource_path, method, query_params,
                                          post_data, header_params, files=files)
        return response

   
