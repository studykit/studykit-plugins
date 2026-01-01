# MoveFeatureTranslateAlongEntityDefinition Object

Derived from: [MoveFeatureDefinition](MoveFeatureDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureTranslateAlongEntityDefinition.h>

## Description

The MoveFeatureTranslateAlongEntityDefinition object defines a move feature described by a translation in the direction defined by a specified entity.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MoveFeatureTranslateAlongEntityDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [distance](MoveFeatureTranslateAlongEntityDefinition_distance.htm) | Gets the model parameter that controls the offset distance. You can use properties on the returned ModelParameter object to edit the offset distance. |
| [isValid](MoveFeatureTranslateAlongEntityDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linearEntity](MoveFeatureTranslateAlongEntityDefinition_linearEntity.htm) | Gets and sets the linear entity that defines the direction of the move. This can be a linear BRepEdge, ConstructionAxis, or a SketchLine. The entity defines the direction, not the distance. The natural direction of the entity defines the translation direction. |
| [objectType](MoveFeatureTranslateAlongEntityDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentMoveFeature](MoveFeatureTranslateAlongEntityDefinition_parentMoveFeature.htm) | Returns the parent MoveFeature object |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |