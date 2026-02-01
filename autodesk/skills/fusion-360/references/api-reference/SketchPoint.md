# SketchPoint Object

Derived from: [SketchEntity](SketchEntity.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPoint.h>

## Description

A point within a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SketchPoint_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](SketchPoint_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](SketchPoint_deleteMe.htm) | Deletes the entity from the sketch. |
| [detach](SketchPoint_detach.htm) | This method disconnects the specified curve from the sketch point. The specified curve must use this point as one of its endpoints, and at least one other sketch curve must also use the point as its endpoint. Detaching the curve creates a new sketch point, which becomes the curve's end point. All other curves using the original sketch point will remain unaffected. |
| [merge](SketchPoint_merge.htm) | Merges the input sketch point into this sketch point. This effectively deletes the other sketch point and changes all entities that referenced that sketch point to reference this sketch point. |
| [move](SketchPoint_move.htm) | Moves the sketch geometry using the specified transform. Move respects any constraints that would normally prohibit the move. This will fail in the case where the IsReference property is true. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](SketchPoint_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](SketchPoint_attributes.htm) | Returns the collection of attributes associated with this face. |
| [boundingBox](SketchPoint_boundingBox.htm) | Returns the bounding box of the entity in sketch space. |
| [connectedEntities](SketchPoint_connectedEntities.htm) | Returns the set of sketch entities that are directly connected to this point. For example any entities that use this point as their start point or end point will be returned and any circle, arc or ellipse who have this point as a center point will be returned. This does not include entities that are related to the point through a constraint. |
| [entityToken](SketchPoint_entityToken.htm) | Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [geometricConstraints](SketchPoint_geometricConstraints.htm) | Returns the sketch constraints that are attached to this curve. |
| [geometry](SketchPoint_geometry.htm) | Returns a Point3D object which provides the position of the sketch point. The returned geometry is always in sketch space. |
| [is2D](SketchPoint_is2D.htm) | Indicates if this curve lies entirely on the sketch x-y plane. |
| [isDeletable](SketchPoint_isDeletable.htm) | Indicates if this sketch entity can be deleted. There are cases, especially with sketch points where another entity is dependent on an entity so deleting it is not allowed. For example, you can't delete the center point of circle by itself but deleting the circle will delete the point. The same is true for the end points of a line. |
| [isFixed](SketchPoint_isFixed.htm) | Indicates if this geometry is "fixed". |
| [isFullyConstrained](SketchPoint_isFullyConstrained.htm) | Indicates if this sketch entity is fully constrained. |
| [isLinked](SketchPoint_isLinked.htm) | Indicates if this sketch entity was created by a projection, inclusion, or driven by an API script. If this returns true, then the entity is presented to the user as not editable and with a 'break link' command available. |
| [isReference](SketchPoint_isReference.htm) | Indicates if this geometry is a reference. Changing this property from true to false removes the reference. This property can not be set to true if it is already false. |
| [isValid](SketchPoint_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](SketchPoint_isVisible.htm) | When a sketch is created, geometry is sometimes automatically added to the sketch. For example a sketch point that references the origin point is always included and if a face was selected to create the sketch on, geometry from the face is also included. This automatically created geometry behaves in a special way in that it is invisible but is available for selection and it also participates in profile calculations. It's not possible to make them visible but they can be deleted and they can be used for any other standard sketch operation. |
| [nativeObject](SketchPoint_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](SketchPoint_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentSketch](SketchPoint_parentSketch.htm) | Returns the parent sketch. |
| [referencedEntity](SketchPoint_referencedEntity.htm) | Returns the referenced entity in the case where IsReference is true. However, this property can also return null when IsReference is true in the case where the reference is not parametric. |
| [sketchDimensions](SketchPoint_sketchDimensions.htm) | Returns the sketch dimensions that are attached to this curve. |
| [worldGeometry](SketchPoint_worldGeometry.htm) | Returns a Point3D object which provides the position of the sketch point in world space. The returned coordinate takes into account the assembly context and the position of the sketch in it's parent component, which means the coordinate will be returned in the root component space. |

## Accessed From

[CircularPatternConstraint.centerPoint](CircularPatternConstraint_centerPoint.htm), [CircularPatternConstraintInput.centerPoint](CircularPatternConstraintInput_centerPoint.htm), [CoincidentConstraint.point](CoincidentConstraint_point.htm), [CoincidentToSurfaceConstraint.point](CoincidentToSurfaceConstraint_point.htm), [HorizontalPointsConstraint.pointOne](HorizontalPointsConstraint_pointOne.htm), [HorizontalPointsConstraint.pointTwo](HorizontalPointsConstraint_pointTwo.htm), [MidPointConstraint.point](MidPointConstraint_point.htm), [PolygonConstraint.centerPoint](PolygonConstraint_centerPoint.htm), [PolygonConstraint.points](PolygonConstraint_points.htm), [SharedPointCoincident.point](SharedPointCoincident_point.htm), [Sketch.originPoint](Sketch_originPoint.htm), [SketchArc.centerSketchPoint](SketchArc_centerSketchPoint.htm), [SketchArc.endSketchPoint](SketchArc_endSketchPoint.htm), [SketchArc.startSketchPoint](SketchArc_startSketchPoint.htm), [SketchCircle.centerSketchPoint](SketchCircle_centerSketchPoint.htm), [SketchConicCurve.apexSketchPoint](SketchConicCurve_apexSketchPoint.htm), [SketchConicCurve.endSketchPoint](SketchConicCurve_endSketchPoint.htm), [SketchConicCurve.startSketchPoint](SketchConicCurve_startSketchPoint.htm), [SketchControlPointSpline.controlPoints](SketchControlPointSpline_controlPoints.htm), [SketchControlPointSpline.endSketchPoint](SketchControlPointSpline_endSketchPoint.htm), [SketchControlPointSpline.startSketchPoint](SketchControlPointSpline_startSketchPoint.htm), [SketchDistanceBetweenPointAndSurfaceDimension.point](SketchDistanceBetweenPointAndSurfaceDimension_point.htm), [SketchEllipse.centerSketchPoint](SketchEllipse_centerSketchPoint.htm), [SketchEllipticalArc.centerSketchPoint](SketchEllipticalArc_centerSketchPoint.htm), [SketchEllipticalArc.endSketchPoint](SketchEllipticalArc_endSketchPoint.htm), [SketchEllipticalArc.startSketchPoint](SketchEllipticalArc_startSketchPoint.htm), [SketchFittedSpline.addFitPoint](SketchFittedSpline_addFitPoint.htm), [SketchFittedSpline.endSketchPoint](SketchFittedSpline_endSketchPoint.htm), [SketchFittedSpline.startSketchPoint](SketchFittedSpline_startSketchPoint.htm), [SketchFixedSpline.endSketchPoint](SketchFixedSpline_endSketchPoint.htm), [SketchFixedSpline.startSketchPoint](SketchFixedSpline_startSketchPoint.htm), [SketchLine.endSketchPoint](SketchLine_endSketchPoint.htm), [SketchLine.startSketchPoint](SketchLine_startSketchPoint.htm), [SketchPoint.createForAssemblyContext](SketchPoint_createForAssemblyContext.htm), [SketchPoint.detach](SketchPoint_detach.htm), [SketchPoint.nativeObject](SketchPoint_nativeObject.htm), [SketchPointHolePositionDefinition.sketchPoint](SketchPointHolePositionDefinition_sketchPoint.htm), [SketchPointList.item](SketchPointList_item.htm), [SketchPoints.add](SketchPoints_add.htm), [SketchPoints.item](SketchPoints_item.htm), [VerticalPointsConstraint.pointOne](VerticalPointsConstraint_pointOne.htm), [VerticalPointsConstraint.pointTwo](VerticalPointsConstraint_pointTwo.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Point API Sample](SketchPointSample_Sample.htm) | Demonstrates creating a new sketch point. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |