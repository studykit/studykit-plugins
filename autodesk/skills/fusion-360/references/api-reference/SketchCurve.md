# SketchCurve Object

Derived from: [SketchEntity](SketchEntity.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurve.h>

## Description

A single sketch curve. This is the base class for the specific curve types.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [breakCurve](SketchCurve_breakCurve.htm) | Breaks a curve into two or three pieces by finding intersections of this curve with all other curves in the sketch and splitting this curve at the nearest intersections to a specified point on the curve. |
| [classType](SketchCurve_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](SketchCurve_deleteMe.htm) | Deletes the entity from the sketch. |
| [extend](SketchCurve_extend.htm) | Extend a curve by specifying a point that determines the end of the curve to extend |
| [intersections](SketchCurve_intersections.htm) | Get the curves that intersect this curve along with the intersection points (Point3D) |
| [split](SketchCurve_split.htm) | Split a curve at a position specified along the curve |
| [trim](SketchCurve_trim.htm) | Trim a curve by specifying a point that determines the segment of the curve to trim away |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](SketchCurve_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](SketchCurve_attributes.htm) | Returns the collection of attributes associated with this face. |
| [boundingBox](SketchCurve_boundingBox.htm) | Returns the bounding box of the entity in sketch space. |
| [entityToken](SketchCurve_entityToken.htm) | Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity. |
| [geometricConstraints](SketchCurve_geometricConstraints.htm) | Returns the sketch constraints that are attached to this curve. |
| [is2D](SketchCurve_is2D.htm) | Indicates if this curve lies entirely on the sketch x-y plane. |
| [isConstruction](SketchCurve_isConstruction.htm) | Gets and sets whether this curve is construction geometry. |
| [isDeletable](SketchCurve_isDeletable.htm) | Indicates if this sketch entity can be deleted. There are cases, especially with sketch points where another entity is dependent on an entity so deleting it is not allowed. For example, you can't delete the center point of circle by itself but deleting the circle will delete the point. The same is true for the end points of a line. |
| [isFixed](SketchCurve_isFixed.htm) | Indicates if this geometry is "fixed". |
| [isFullyConstrained](SketchCurve_isFullyConstrained.htm) | Indicates if this sketch entity is fully constrained. |
| [isLinked](SketchCurve_isLinked.htm) | Indicates if this sketch entity was created by a projection, inclusion, or driven by an API script. If this returns true, then the entity is presented to the user as not editable and with a 'break link' command available. |
| [isReference](SketchCurve_isReference.htm) | Indicates if this geometry is a reference. Changing this property from true to false removes the reference. This property can not be set to true if it is already false. |
| [isValid](SketchCurve_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](SketchCurve_isVisible.htm) | When a sketch is created, geometry is sometimes automatically added to the sketch. For example a sketch point that references the origin point is always included and if a face was selected to create the sketch on, geometry from the face is also included. This automatically created geometry behaves in a special way in that it is invisible but is available for selection and it also participates in profile calculations. It's not possible to make them visible but they can be deleted and they can be used for any other standard sketch operation. |
| [length](SketchCurve_length.htm) | Returns the length of the curve in centimeters. |
| [objectType](SketchCurve_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentSketch](SketchCurve_parentSketch.htm) | Returns the parent sketch. |
| [referencedEntity](SketchCurve_referencedEntity.htm) | Returns the referenced entity in the case where IsReference is true. However, this property can also return null when IsReference is true in the case where the reference is not parametric. |
| [sketchDimensions](SketchCurve_sketchDimensions.htm) | Returns the sketch dimensions that are attached to this curve. |

## Accessed From

[ConcentricConstraint.entityOne](ConcentricConstraint_entityOne.htm), [ConcentricConstraint.entityTwo](ConcentricConstraint_entityTwo.htm), [EqualConstraint.curveOne](EqualConstraint_curveOne.htm), [EqualConstraint.curveTwo](EqualConstraint_curveTwo.htm), [MidPointConstraint.midPointCurve](MidPointConstraint_midPointCurve.htm), [OffsetConstraint.childCurves](OffsetConstraint_childCurves.htm), [OffsetConstraint.parentCurves](OffsetConstraint_parentCurves.htm), [OffsetConstraintInput.curves](OffsetConstraintInput_curves.htm), [PerpendicularToSurfaceConstraint.curve](PerpendicularToSurfaceConstraint_curve.htm), [SharedPointCoincident.curveOne](SharedPointCoincident_curveOne.htm), [SharedPointCoincident.curveTwo](SharedPointCoincident_curveTwo.htm), [SketchConcentricCircleDimension.circleOne](SketchConcentricCircleDimension_circleOne.htm), [SketchConcentricCircleDimension.circleTwo](SketchConcentricCircleDimension_circleTwo.htm), [SketchCurves.item](SketchCurves_item.htm), [SketchDiameterDimension.entity](SketchDiameterDimension_entity.htm), [SketchEllipseMajorRadiusDimension.ellipse](SketchEllipseMajorRadiusDimension_ellipse.htm), [SketchEllipseMinorRadiusDimension.ellipse](SketchEllipseMinorRadiusDimension_ellipse.htm), [SketchRadialDimension.entity](SketchRadialDimension_entity.htm), [SketchTangentDistanceDimension.circleOrArc](SketchTangentDistanceDimension_circleOrArc.htm), [SketchText.explode](SketchText_explode.htm), [SmoothConstraint.curveOne](SmoothConstraint_curveOne.htm), [SmoothConstraint.curveTwo](SmoothConstraint_curveTwo.htm), [TangentConstraint.curveOne](TangentConstraint_curveOne.htm), [TangentConstraint.curveTwo](TangentConstraint_curveTwo.htm)

## Derived Classes

[SketchArc](SketchArc.htm), [SketchCircle](SketchCircle.htm), [SketchConicCurve](SketchConicCurve.htm), [SketchControlPointSpline](SketchControlPointSpline.htm), [SketchEllipse](SketchEllipse.htm), [SketchEllipticalArc](SketchEllipticalArc.htm), [SketchFittedSpline](SketchFittedSpline.htm), [SketchFixedSpline](SketchFixedSpline.htm), [SketchLine](SketchLine.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |