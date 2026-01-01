# Arrange3DDefinition Object

Derived from: [ArrangeDefinition](ArrangeDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange3DDefinition.h>

## Description

This object defines all of the settings associated with a 3D arrangement.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Arrange3DDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isCreateCopies](Arrange3DDefinition_isCreateCopies.htm) | Gets if the original components were moved to create the arrangement or copied were created. This value can only be set when creating a new arrangement. |
| [isValid](Arrange3DDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Arrange3DDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [solverType](Arrange3DDefinition_solverType.htm) | Gets the type of arrange feature defined by this definition. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |