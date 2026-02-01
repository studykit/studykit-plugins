# SketchFixedSpline Object

Derived from: [SketchCurve](SketchCurve.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFixedSpline.h>

## Description

The SketchFixedSpline class represents splines in a sketch that are not editable. These can result from including splines from other sketches or the spline edges. They can also be created by intersections and projecting splines onto a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [breakCurve](SketchFixedSpline_breakCurve.htm) | Breaks a curve into two or three pieces by finding intersections of this curve with all other curves in the sketch and splitting this curve at the nearest intersections to a specified point on the curve. |
| [classType](SketchFixedSpline_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](SketchFixedSpline_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](SketchFixedSpline_deleteMe.htm) | Deletes the entity from the sketch. |
| [extend](SketchFixedSpline_extend.htm) | Extend a curve by specifying a point that determines the end of the curve to extend |
| [intersections](SketchFixedSpline_intersections.htm) | Get the curves that intersect this curve along with the intersection points (Point3D) |
| [replaceGeometry](SketchFixedSpline_replaceGeometry.htm) | Replaces the underlying NURBS curve that defines the shape of the fixed curve. This can only be used if the isNative property of the SketchFixedSpline returns false. |
| [split](SketchFixedSpline_split.htm) | Split a curve at a position specified along the curve |
| [trim](SketchFixedSpline_trim.htm) | Trim a curve by specifying a point that determines the segment of the curve to trim away |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](SketchFixedSpline_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](SketchFixedSpline_attributes.htm) | Returns the collection of attributes associated with this face. |
| [boundingBox](SketchFixedSpline_boundingBox.htm) | Returns the bounding box of the entity in sketch space. |
| [endSketchPoint](SketchFixedSpline_endSketchPoint.htm) | The sketch point at the end of the spline. |
| [entityToken](SketchFixedSpline_entityToken.htm) | Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity. |
| [evaluator](SketchFixedSpline_evaluator.htm) | Returns an evaluator object that lets you perform evaluations on the precise geometry of the curve. |
| [geometricConstraints](SketchFixedSpline_geometricConstraints.htm) | Returns the sketch constraints that are attached to this curve. |
| [geometry](SketchFixedSpline_geometry.htm) | Returns the transient geometry of the curve which provides geometric information about the curve. The returned geometry is always in sketch space.   Because the fixed spline can be analytically defined, for example it can be the precise intersection of a surface and the sketch plane, returning a NURBS curve that represents the spline may be an approximation of the actual curve. You can use the Evaluator property of the SketchFixedSpline object to perform evaluations on the precise curve. |
| [is2D](SketchFixedSpline_is2D.htm) | Indicates if this curve lies entirely on the sketch x-y plane. |
| [isConstruction](SketchFixedSpline_isConstruction.htm) | Gets and sets whether this curve is construction geometry. |
| [isDeletable](SketchFixedSpline_isDeletable.htm) | Indicates if this sketch entity can be deleted. There are cases, especially with sketch points where another entity is dependent on an entity so deleting it is not allowed. For example, you can't delete the center point of circle by itself but deleting the circle will delete the point. The same is true for the end points of a line. |
| [isFixed](SketchFixedSpline_isFixed.htm) | Indicates if this geometry is "fixed". |
| [isFullyConstrained](SketchFixedSpline_isFullyConstrained.htm) | Indicates if this sketch entity is fully constrained. |
| [isLinked](SketchFixedSpline_isLinked.htm) | Indicates if this sketch entity was created by a projection, inclusion, or driven by an API script. If this returns true, then the entity is presented to the user as not editable and with a 'break link' command available. |
| [isReference](SketchFixedSpline_isReference.htm) | Indicates if this geometry is a reference. Changing this property from true to false removes the reference. This property can not be set to true if it is already false. |
| [isValid](SketchFixedSpline_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](SketchFixedSpline_isVisible.htm) | When a sketch is created, geometry is sometimes automatically added to the sketch. For example a sketch point that references the origin point is always included and if a face was selected to create the sketch on, geometry from the face is also included. This automatically created geometry behaves in a special way in that it is invisible but is available for selection and it also participates in profile calculations. It's not possible to make them visible but they can be deleted and they can be used for any other standard sketch operation. |
| [length](SketchFixedSpline_length.htm) | Returns the length of the curve in centimeters. |
| [nativeObject](SketchFixedSpline_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](SketchFixedSpline_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentSketch](SketchFixedSpline_parentSketch.htm) | Returns the parent sketch. |
| [referencedEntity](SketchFixedSpline_referencedEntity.htm) | Returns the referenced entity in the case where IsReference is true. However, this property can also return null when IsReference is true in the case where the reference is not parametric. |
| [sketchDimensions](SketchFixedSpline_sketchDimensions.htm) | Returns the sketch dimensions that are attached to this curve. |
| [startSketchPoint](SketchFixedSpline_startSketchPoint.htm) | The sketch point at the start of the spline. |
| [worldGeometry](SketchFixedSpline_worldGeometry.htm) | Returns a NurbsCurve3D object that is the equivalent of this sketch curve but is in the space of the parent component rather than in sketch space. |

## Accessed From

[SketchFixedSpline.createForAssemblyContext](SketchFixedSpline_createForAssemblyContext.htm), [SketchFixedSpline.nativeObject](SketchFixedSpline_nativeObject.htm), [SketchFixedSplines.addByNurbsCurve](SketchFixedSplines_addByNurbsCurve.htm), [SketchFixedSplines.item](SketchFixedSplines_item.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |