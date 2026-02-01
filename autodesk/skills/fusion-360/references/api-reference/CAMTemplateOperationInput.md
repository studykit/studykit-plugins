# CAMTemplateOperationInput Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplateOperationInput.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

A CAMTemplateOperationInput provides access to Operation Template parameters for editing, in much the same way as OperationInput provides access to Operation parameters for editing. Operation Template parameters are slightly different from Operation parameters, for instance in terms of how tools and geometry selections can be specified, so an OperationInput for a given strategy type has a slightly different set of parameters from a CAMTemplateOperationInput for that same strategy type.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CAMTemplateOperationInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [isGeometryIndexEnabled](CAMTemplateOperationInput_isGeometryIndexEnabled.htm) | Get whether a geometry index is selected. |
| [setGeometryIndexEnabled](CAMTemplateOperationInput_setGeometryIndexEnabled.htm) | Set whether a geometry index is selected. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [displayName](CAMTemplateOperationInput_displayName.htm) | Optionally specify the display name that appears in the browser-tree to override the default. |
| [geometryIndexCount](CAMTemplateOperationInput_geometryIndexCount.htm) | Get the number of geometry indices that can be selected. |
| [isValid](CAMTemplateOperationInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CAMTemplateOperationInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parameters](CAMTemplateOperationInput_parameters.htm) | Get all parameters for the current strategy. Parameters are initialized by user defaults. Configure operation parameters before creation for a better performance. |
| [strategy](CAMTemplateOperationInput_strategy.htm) | Get the current strategy |
| [tool](CAMTemplateOperationInput_tool.htm) | Optionally specify the tool used by the operation. The ToolLibraries allows the access to Local and Fusion tools. |
| [toolPreset](CAMTemplateOperationInput_toolPreset.htm) | Optionally specify the preset of the tool. If no preset is specified, the operation gets its default feed and speed. The Tool provides access to available presets. Use one of those presets to override the default. An invalid preset will cause a failure during the creation of the operation. |

## Accessed From

[CAMTemplateOperations.get](CAMTemplateOperations_get.htm), [CAMTemplateOperations.makeInput](CAMTemplateOperations_makeInput.htm)

## Version

Introduced in version March 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |