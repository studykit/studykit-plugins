# PostProcessingMachineElement Object ![Preview](../images/TestTubeLarge.png)

Derived from: [MachineElement](MachineElement.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/PostProcessingMachineElement.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Machine element representing the post processor and post properties.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PostProcessingMachineElement_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [staticTypeId](PostProcessingMachineElement_staticTypeId.htm) | Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type. |
| [updatePostParameters](PostProcessingMachineElement_updatePostParameters.htm) | Overrides the default post parameters with the given user's input. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [elementId](PostProcessingMachineElement_elementId.htm) | Identifier for this element. Unique within an element type. |
| [isValid](PostProcessingMachineElement_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](PostProcessingMachineElement_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [outputFolder](PostProcessingMachineElement_outputFolder.htm) | Gets and sets the path for the output folder where the .nc files will be located. |
| [postParameters](PostProcessingMachineElement_postParameters.htm) | Gets the machine scope post properties as parameters. |
| [postURL](PostProcessingMachineElement_postURL.htm) | Gets or sets the URL of the post assigned to the machine. |
| [typeId](PostProcessingMachineElement_typeId.htm) | Identifier for this type of machine element. |

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |