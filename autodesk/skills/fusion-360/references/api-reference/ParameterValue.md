# ParameterValue Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Operations/ParameterValue.h>

## Description

Base class for representing the value of a parameter. Subclasses implement value handling for available parameter types.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ParameterValue_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ParameterValue_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ParameterValue_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](ParameterValue_parent.htm) | Get the parameter object that the value is associated with. |

## Accessed From

[CAMParameter.value](CAMParameter_value.htm)

## Derived Classes

[BooleanParameterValue](BooleanParameterValue.htm), [CadContours2dParameterValue](CadContours2dParameterValue.htm), [CadMachineAvoidGroupsParameterValue](CadMachineAvoidGroupsParameterValue.htm), [CadObjectParameterValue](CadObjectParameterValue.htm), [CAMArrangeParameterValue](CAMArrangeParameterValue.htm), [ChoiceParameterValue](ChoiceParameterValue.htm), [FloatParameterValue](FloatParameterValue.htm), [IntegerParameterValue](IntegerParameterValue.htm), [StringParameterValue](StringParameterValue.htm)

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |