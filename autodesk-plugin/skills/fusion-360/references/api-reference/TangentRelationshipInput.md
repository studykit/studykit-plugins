# TangentRelationshipInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationshipInput.h>

## Description

Defines all of the information required to create a new tangent relationship. This object provides equivalent functionality to the Tangent Relationship command dialog in that it gathers the required information to create a tangent relationship.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](TangentRelationshipInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [faceOne](TangentRelationshipInput_faceOne.htm) | Gets and sets the first BRepFace object that will remain tangent to the set of specified tangent faces. |
| [isValid](TangentRelationshipInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](TangentRelationshipInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [tangentFaces](TangentRelationshipInput_tangentFaces.htm) | Gets and sets a single BRepFace object that is part of the body that faceOne will remain tangent to. All of the faces of the body will be used when computing the tangent relationship. |

## Accessed From

[TangentRelationships.createInput](TangentRelationships_createInput.htm)

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |