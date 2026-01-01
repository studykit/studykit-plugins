# ArrangeDefinition3DInput Object

Derived from: [ArrangeDefinitionInput](ArrangeDefinitionInput.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeDefinition3DInput.h>

## Description

This object defines all of the settings associated with a 3D arrangement.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ArrangeDefinition3DInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isCreateCopies](ArrangeDefinition3DInput_isCreateCopies.htm) | Gets and set if the original components will be moved or copied to create the arrangement. This defaults to true. |
| [isValid](ArrangeDefinition3DInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ArrangeDefinition3DInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [solverType](ArrangeDefinition3DInput_solverType.htm) | Gets the type of arrange feature defined by this definition. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |