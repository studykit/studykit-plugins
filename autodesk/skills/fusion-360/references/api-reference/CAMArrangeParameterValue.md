# CAMArrangeParameterValue Object

Derived from: [ParameterValue](ParameterValue.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CAMArrangeParameterValue.h>

## Description

A parameter value that is a CAMArrangeParameterValue. The user needs to set the parameter anew via the API after a model update or after the ArrangeSelections returned by getArrangeSelections() have been edited.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [applyArrangeSelections](CAMArrangeParameterValue_applyArrangeSelections.htm) | Set the values of the parameter as a collection of CadObjects. |
| [classType](CAMArrangeParameterValue_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [getArrangeSelections](CAMArrangeParameterValue_getArrangeSelections.htm) | Get the values of the parameter as a collection of CadObjects, which currently consist of occurrences. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](CAMArrangeParameterValue_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CAMArrangeParameterValue_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](CAMArrangeParameterValue_parent.htm) | Get the parameter object that the value is associated with. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |