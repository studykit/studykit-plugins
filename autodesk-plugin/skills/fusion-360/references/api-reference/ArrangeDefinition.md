# ArrangeDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeDefinition.h>

## Description

The ArrangeDefinition object is the base class for the ArrangeDefinition2D and ArrangeDefinition3D objects. It provides access to the information that defines an existing Arrange feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ArrangeDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isCreateCopies](ArrangeDefinition_isCreateCopies.htm) | Gets if the original components were moved to create the arrangement or copied were created. This value can only be set when creating a new arrangement. |
| [isValid](ArrangeDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ArrangeDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [solverType](ArrangeDefinition_solverType.htm) | Gets the type of arrange feature defined by this definition. |

## Accessed From

[ArrangeFeature.definition](ArrangeFeature_definition.htm)

## Derived Classes

[Arrange2DDefinition](Arrange2DDefinition.htm), [Arrange3DDefinition](Arrange3DDefinition.htm)

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |