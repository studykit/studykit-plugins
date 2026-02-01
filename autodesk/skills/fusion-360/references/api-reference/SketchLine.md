# SketchLine Object

Derived from: [SketchCurve](SketchCurve.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLine.h>

## Description

A line in a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [breakCurve](SketchLine_breakCurve.htm) | Breaks a curve into two or three pieces by finding intersections of this curve with all other curves in the sketch and splitting this curve at the nearest intersections to a specified point on the curve. |
| [classType](SketchLine_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](SketchLine_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](SketchLine_deleteMe.htm) | Deletes the entity from the sketch. |
| [extend](SketchLine_extend.htm) | Extend a curve by specifying a point that determines the end of the curve to extend |
| [intersections](SketchLine_intersections.htm) | Get the curves that intersect this curve along with the intersection points (Point3D) |
| [split](SketchLine_split.htm) | Split a curve at a position specified along the curve |
| [trim](SketchLine_trim.htm) | Trim a curve by specifying a point that determines the segment of the curve to trim away |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](SketchLine_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](SketchLine_attributes.htm) | Returns the collection of attributes associated with this face. |
| [boundingBox](SketchLine_boundingBox.htm) | Returns the bounding box of the entity in sketch space. |
| [endSketchPoint](SketchLine_endSketchPoint.htm) | The sketch point at the end of the line. The line is dependent on this point and moving the point will cause the line to adjust. |
| [entityToken](SketchLine_entityToken.htm) | Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity. |
| [geometricConstraints](SketchLine_geometricConstraints.htm) | Returns the sketch constraints that are attached to this curve. |
| [geometry](SketchLine_geometry.htm) | Returns the transient geometry of the line which provides geometry information about the line. The returned geometry is always in sketch space. |
| [is2D](SketchLine_is2D.htm) | Indicates if this curve lies entirely on the sketch x-y plane. |
| [isCenterLine](SketchLine_isCenterLine.htm) | Gets and sets whether this line is defined as a centerline. |
| [isConstruction](SketchLine_isConstruction.htm) | Gets and sets whether this curve is construction geometry. |
| [isDeletable](SketchLine_isDeletable.htm) | Indicates if this sketch entity can be deleted. There are cases, especially with sketch points where another entity is dependent on an entity so deleting it is not allowed. For example, you can't delete the center point of circle by itself but deleting the circle will delete the point. The same is true for the end points of a line. |
| [isFixed](SketchLine_isFixed.htm) | Indicates if this geometry is "fixed". |
| [isFullyConstrained](SketchLine_isFullyConstrained.htm) | Indicates if this sketch entity is fully constrained. |
| [isLinked](SketchLine_isLinked.htm) | Indicates if this sketch entity was created by a projection, inclusion, or driven by an API script. If this returns true, then the entity is presented to the user as not editable and with a 'break link' command available. |
| [isReference](SketchLine_isReference.htm) | Indicates if this geometry is a reference. Changing this property from true to false removes the reference. This property can not be set to true if it is already false. |
| [isValid](SketchLine_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](SketchLine_isVisible.htm) | When a sketch is created, geometry is sometimes automatically added to the sketch. For example a sketch point that references the origin point is always included and if a face was selected to create the sketch on, geometry from the face is also included. This automatically created geometry behaves in a special way in that it is invisible but is available for selection and it also participates in profile calculations. It's not possible to make them visible but they can be deleted and they can be used for any other standard sketch operation. |
| [length](SketchLine_length.htm) | Returns the length of the curve in centimeters. |
| [nativeObject](SketchLine_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](SketchLine_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentSketch](SketchLine_parentSketch.htm) | Returns the parent sketch. |
| [referencedEntity](SketchLine_referencedEntity.htm) | Returns the referenced entity in the case where IsReference is true. However, this property can also return null when IsReference is true in the case where the reference is not parametric. |
| [sketchDimensions](SketchLine_sketchDimensions.htm) | Returns the sketch dimensions that are attached to this curve. |
| [startSketchPoint](SketchLine_startSketchPoint.htm) | The sketch point at the start of the line. The line is dependent on this point and moving the point will cause the line to adjust. |
| [worldGeometry](SketchLine_worldGeometry.htm) | Returns a Line3D object which provides geometric information in world space. The returned geometry takes into account the assembly context and the position of the sketch in it's parent component, which means the geometry will be returned in the root component space. |

## Accessed From

[CollinearConstraint.lineOne](CollinearConstraint_lineOne.htm), [CollinearConstraint.lineTwo](CollinearConstraint_lineTwo.htm), [HorizontalConstraint.line](HorizontalConstraint_line.htm), [LineOnPlanarSurfaceConstraint.line](LineOnPlanarSurfaceConstraint_line.htm), [LineParallelToPlanarSurfaceConstraint.line](LineParallelToPlanarSurfaceConstraint_line.htm), [MultiLineTextDefinition.rectangleLines](MultiLineTextDefinition_rectangleLines.htm), [ParallelConstraint.lineOne](ParallelConstraint_lineOne.htm), [ParallelConstraint.lineTwo](ParallelConstraint_lineTwo.htm), [PerpendicularConstraint.lineOne](PerpendicularConstraint_lineOne.htm), [PerpendicularConstraint.lineTwo](PerpendicularConstraint_lineTwo.htm), [PolygonConstraint.lines](PolygonConstraint_lines.htm), [RectangularPatternConstraint.directionOneEntity](RectangularPatternConstraint_directionOneEntity.htm), [RectangularPatternConstraint.directionTwoEntity](RectangularPatternConstraint_directionTwoEntity.htm), [RectangularPatternConstraintInput.directionOneEntity](RectangularPatternConstraintInput_directionOneEntity.htm), [RectangularPatternConstraintInput.directionTwoEntity](RectangularPatternConstraintInput_directionTwoEntity.htm), [SketchAngularDimension.lineOne](SketchAngularDimension_lineOne.htm), [SketchAngularDimension.lineTwo](SketchAngularDimension_lineTwo.htm), [SketchControlPointSpline.controlFrameLines](SketchControlPointSpline_controlFrameLines.htm), [SketchDistanceBetweenLineAndPlanarSurfaceDimension.line](SketchDistanceBetweenLineAndPlanarSurfaceDimension_line.htm), [SketchEllipse.majorAxisLine](SketchEllipse_majorAxisLine.htm), [SketchEllipse.minorAxisLine](SketchEllipse_minorAxisLine.htm), [SketchFittedSpline.activateTangentHandle](SketchFittedSpline_activateTangentHandle.htm), [SketchFittedSpline.getTangentHandle](SketchFittedSpline_getTangentHandle.htm), [SketchLine.createForAssemblyContext](SketchLine_createForAssemblyContext.htm), [SketchLine.nativeObject](SketchLine_nativeObject.htm), [SketchLinearDiameterDimension.line](SketchLinearDiameterDimension_line.htm), [SketchLineList.item](SketchLineList_item.htm), [SketchLines.addAngleChamfer](SketchLines_addAngleChamfer.htm), [SketchLines.addByTwoPoints](SketchLines_addByTwoPoints.htm), [SketchLines.addDistanceChamfer](SketchLines_addDistanceChamfer.htm), [SketchLines.item](SketchLines_item.htm), [SketchOffsetDimension.line](SketchOffsetDimension_line.htm), [SymmetryConstraint.symmetryLine](SymmetryConstraint_symmetryLine.htm), [VerticalConstraint.line](VerticalConstraint_line.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |