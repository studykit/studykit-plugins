# SketchEntity Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEntity.h>

## Description

This object represents all geometry in a sketch, including all the various curves, points, and text.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SketchEntity_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](SketchEntity_deleteMe.htm) | Deletes the entity from the sketch. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](SketchEntity_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](SketchEntity_attributes.htm) | Returns the collection of attributes associated with this face. |
| [boundingBox](SketchEntity_boundingBox.htm) | Returns the bounding box of the entity in sketch space. |
| [entityToken](SketchEntity_entityToken.htm) | Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity. |
| [geometricConstraints](SketchEntity_geometricConstraints.htm) | Returns the sketch constraints that are attached to this curve. |
| [is2D](SketchEntity_is2D.htm) | Indicates if this curve lies entirely on the sketch x-y plane. |
| [isDeletable](SketchEntity_isDeletable.htm) | Indicates if this sketch entity can be deleted. There are cases, especially with sketch points where another entity is dependent on an entity so deleting it is not allowed. For example, you can't delete the center point of circle by itself but deleting the circle will delete the point. The same is true for the end points of a line. |
| [isFixed](SketchEntity_isFixed.htm) | Indicates if this geometry is "fixed". |
| [isFullyConstrained](SketchEntity_isFullyConstrained.htm) | Indicates if this sketch entity is fully constrained. |
| [isLinked](SketchEntity_isLinked.htm) | Indicates if this sketch entity was created by a projection, inclusion, or driven by an API script. If this returns true, then the entity is presented to the user as not editable and with a 'break link' command available. |
| [isReference](SketchEntity_isReference.htm) | Indicates if this geometry is a reference. Changing this property from true to false removes the reference. This property can not be set to true if it is already false. |
| [isValid](SketchEntity_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](SketchEntity_isVisible.htm) | When a sketch is created, geometry is sometimes automatically added to the sketch. For example a sketch point that references the origin point is always included and if a face was selected to create the sketch on, geometry from the face is also included. This automatically created geometry behaves in a special way in that it is invisible but is available for selection and it also participates in profile calculations. It's not possible to make them visible but they can be deleted and they can be used for any other standard sketch operation. |
| [objectType](SketchEntity_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentSketch](SketchEntity_parentSketch.htm) | Returns the parent sketch. |
| [referencedEntity](SketchEntity_referencedEntity.htm) | Returns the referenced entity in the case where IsReference is true. However, this property can also return null when IsReference is true in the case where the reference is not parametric. |
| [sketchDimensions](SketchEntity_sketchDimensions.htm) | Returns the sketch dimensions that are attached to this curve. |

## Accessed From

[CircularPatternConstraint.createdEntities](CircularPatternConstraint_createdEntities.htm), [CircularPatternConstraint.entities](CircularPatternConstraint_entities.htm), [CircularPatternConstraintInput.entities](CircularPatternConstraintInput_entities.htm), [CoincidentConstraint.entity](CoincidentConstraint_entity.htm), [ProfileCurve.sketchEntity](ProfileCurve_sketchEntity.htm), [RectangularPatternConstraint.createdEntities](RectangularPatternConstraint_createdEntities.htm), [RectangularPatternConstraint.entities](RectangularPatternConstraint_entities.htm), [RectangularPatternConstraintInput.entities](RectangularPatternConstraintInput_entities.htm), [Sketch.createSpunProfile](Sketch_createSpunProfile.htm), [Sketch.intersectWithSketchPlane](Sketch_intersectWithSketchPlane.htm), [Sketch.project2](Sketch_project2.htm), [Sketch.projectToSurface](Sketch_projectToSurface.htm), [SketchEntityList.item](SketchEntityList_item.htm), [SketchLinearDiameterDimension.entityTwo](SketchLinearDiameterDimension_entityTwo.htm), [SketchLinearDimension.entityOne](SketchLinearDimension_entityOne.htm), [SketchLinearDimension.entityTwo](SketchLinearDimension_entityTwo.htm), [SketchOffsetDimension.entityTwo](SketchOffsetDimension_entityTwo.htm), [SketchTangentDistanceDimension.entityOne](SketchTangentDistanceDimension_entityOne.htm), [SymmetryConstraint.entityOne](SymmetryConstraint_entityOne.htm), [SymmetryConstraint.entityTwo](SymmetryConstraint_entityTwo.htm)

## Derived Classes

[SketchCurve](SketchCurve.htm), [SketchPoint](SketchPoint.htm), [SketchText](SketchText.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |