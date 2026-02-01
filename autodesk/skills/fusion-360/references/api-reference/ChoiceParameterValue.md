# ChoiceParameterValue Object

Derived from: [ParameterValue](ParameterValue.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Operations/ChoiceParameterValue.h>

## Description

A parameter value that is a list of choices.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ChoiceParameterValue_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [getChoices](ChoiceParameterValue_getChoices.htm) | Method that returns the list of available choices. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ChoiceParameterValue_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ChoiceParameterValue_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](ChoiceParameterValue_parent.htm) | Get the parameter object that the value is associated with. |
| [value](ChoiceParameterValue_value.htm) | Get or set the value of the parameter. This value will correspond to one of the available values of the parameter. |

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |