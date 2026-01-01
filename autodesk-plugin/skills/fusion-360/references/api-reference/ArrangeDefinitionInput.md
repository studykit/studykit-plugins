# ArrangeDefinitionInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeDefinitionInput.h>

## Description

The ArrangeDefinition object is the base class for the ArrangeDefinition2D and ArrangeDefinition3D objects. It provides access to the information that defines an existing Arrange feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ArrangeDefinitionInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isCreateCopies](ArrangeDefinitionInput_isCreateCopies.htm) | Gets and set if the original components will be moved or copied to create the arrangement. This defaults to true. |
| [isValid](ArrangeDefinitionInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ArrangeDefinitionInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [solverType](ArrangeDefinitionInput_solverType.htm) | Gets the type of arrange feature defined by this definition. |

## Accessed From

[ArrangeFeatureInput.definition](ArrangeFeatureInput_definition.htm)

## Derived Classes

[ArrangeDefinition2DInput](ArrangeDefinition2DInput.htm), [ArrangeDefinition3DInput](ArrangeDefinition3DInput.htm)

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |