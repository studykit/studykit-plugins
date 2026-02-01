# TangentRelationship Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationship.h>

## Description

A tangent relationship in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](TangentRelationship_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](TangentRelationship_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](TangentRelationship_deleteMe.htm) | Deletes this tangent relationship. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](TangentRelationship_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](TangentRelationship_attributes.htm) | Returns the collection of attributes associated with this tangent relationship. |
| [entityToken](TangentRelationship_entityToken.htm) | Returns a token for the TangentRelationship object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same tangent relationship. |
| [errorOrWarningMessage](TangentRelationship_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [faceOne](TangentRelationship_faceOne.htm) | Gets and sets the first BRepFace object that will remain tangent to the set of specified tangent faces.   To set this property, you need to position the timeline marker to immediately before this tangent relationship. This can be accomplished using the following code: thisTangentRelationship.timelineObject.rollTo(True) |
| [healthState](TangentRelationship_healthState.htm) | Returns the current health state of the tangent relationship. |
| [isSuppressed](TangentRelationship_isSuppressed.htm) | Gets and sets if this tangent relationship is suppressed. |
| [isValid](TangentRelationship_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](TangentRelationship_name.htm) | Gets and sets the name of the tangent relationship. |
| [nativeObject](TangentRelationship_nativeObject.htm) | The native object is the tangent relationship in the context of the component it was created within.   Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](TangentRelationship_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [occurrenceOne](TangentRelationship_occurrenceOne.htm) | Returns the first of two occurrences that this tangent relationship defines a relationship between. |
| [occurrenceTwo](TangentRelationship_occurrenceTwo.htm) | Returns the second of two occurrences that this tangent relationship defines a relationship between. |
| [parentComponent](TangentRelationship_parentComponent.htm) | Returns the parent component that owns this tangent relationship. |
| [tangentFaces](TangentRelationship_tangentFaces.htm) | Gets and sets a single BRepFace object that is part of the body that faceOne will remain tangent to. All of the faces of the body will be used when computing the tangent relationship.   To set this property, you need to position the timeline marker to immediately before this tangent relationship. This can be accomplished using the following code: thisTangentRelationship.timelineObject.rollTo(True) |
| [timelineObject](TangentRelationship_timelineObject.htm) | Returns the timeline object associated with this tangent relationship. |

## Accessed From

[Component.allTangentRelationships](Component_allTangentRelationships.htm), [FlatPatternComponent.allTangentRelationships](FlatPatternComponent_allTangentRelationships.htm), [TangentRelationship.createForAssemblyContext](TangentRelationship_createForAssemblyContext.htm), [TangentRelationship.nativeObject](TangentRelationship_nativeObject.htm), [TangentRelationships.add](TangentRelationships_add.htm), [TangentRelationships.item](TangentRelationships_item.htm), [TangentRelationships.itemByName](TangentRelationships_itemByName.htm)

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |