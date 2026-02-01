# PostConfiguration Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostConfiguration.h>

## Description

Object that represents a post configuration.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PostConfiguration_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [capability](PostConfiguration_capability.htm) | Gets the capabilities supported by the post. Capabilities define what types of operations can be post processed using this configuration. |
| [description](PostConfiguration_description.htm) | Gets the description of the post. |
| [extension](PostConfiguration_extension.htm) | Gets the extension of the output file created by the post. |
| [isValid](PostConfiguration_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](PostConfiguration_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [vendor](PostConfiguration_vendor.htm) | Gets the name of the vendor of the machine tool or controller this post configuration supports. |
| [version](PostConfiguration_version.htm) | Gets the version of the post. |

## Accessed From

[NCProgram.postConfiguration](NCProgram_postConfiguration.htm), [PostConfigurationQuery.execute](PostConfigurationQuery_execute.htm), [PostLibrary.childPostConfigurations](PostLibrary_childPostConfigurations.htm), [PostLibrary.postConfigurationAtURL](PostLibrary_postConfigurationAtURL.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |
| [Turning Workflow API Sample](Turning_Workflow_API_Sample_Sample.htm) | Turning Workflow API Sample This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |