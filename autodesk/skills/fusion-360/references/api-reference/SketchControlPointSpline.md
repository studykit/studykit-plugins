# SketchControlPointSpline Object

Derived from: [SketchCurve](SketchCurve.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchControlPointSpline.h>

## Description

A control point spline in a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addControlPoint](SketchControlPointSpline_addControlPoint.htm) | Adds an additional control point to the control point spline. Inserting a new control point does not change the shape of the curve, but the control frame will be re-computed and the control points will be adjusted to maintain the current shape. |
| [breakCurve](SketchControlPointSpline_breakCurve.htm) | Breaks a curve into two or three pieces by finding intersections of this curve with all other curves in the sketch and splitting this curve at the nearest intersections to a specified point on the curve. |
| [classType](SketchControlPointSpline_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](SketchControlPointSpline_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](SketchControlPointSpline_deleteMe.htm) | Deletes the entity from the sketch. |
| [extend](SketchControlPointSpline_extend.htm) | Extend a curve by specifying a point that determines the end of the curve to extend |
| [intersections](SketchControlPointSpline_intersections.htm) | Get the curves that intersect this curve along with the intersection points (Point3D) |
| [split](SketchControlPointSpline_split.htm) | Split a curve at a position specified along the curve |
| [trim](SketchControlPointSpline_trim.htm) | Trim a curve by specifying a point that determines the segment of the curve to trim away |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](SketchControlPointSpline_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](SketchControlPointSpline_attributes.htm) | Returns the collection of attributes associated with this face. |
| [boundingBox](SketchControlPointSpline_boundingBox.htm) | Returns the bounding box of the entity in sketch space. |
| [controlFrameLines](SketchControlPointSpline_controlFrameLines.htm) | Returns the sketch lines that represent the control frame of the spline. The lines are in sequential order starting with the line that connects to the starting control point to the end. |
| [controlPoints](SketchControlPointSpline_controlPoints.htm) | Returns the set of sketch points that the control frame of the spline fits through. The points include the start and end points and are returned in the same order as the spline fits through them where the first point in the list is the start point and the last point is the end point. Editing the position of these sketch points will result in editing the spline.   Deleting one of the sketch points will remove that point from the control frame and the curve will be recomputed. |
| [degree](SketchControlPointSpline_degree.htm) | Gets and sets the degree of the spline. |
| [endSketchPoint](SketchControlPointSpline_endSketchPoint.htm) | The sketch point at the end of the spline. If the curve is closed the start and end sketch points will be the same. |
| [entityToken](SketchControlPointSpline_entityToken.htm) | Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [evaluator](SketchControlPointSpline_evaluator.htm) | Returns an evaluator object that lets you perform evaluations on the precise geometry of the curve. |
| [geometricConstraints](SketchControlPointSpline_geometricConstraints.htm) | Returns the sketch constraints that are attached to this curve. |
| [geometry](SketchControlPointSpline_geometry.htm) | Returns the transient geometry of the curve which provides geometric information about the curve. The returned geometry is always in sketch space. Use the worldGeometry property to get it in the model's design space. |
| [is2D](SketchControlPointSpline_is2D.htm) | Indicates if this curve lies entirely on the sketch x-y plane. |
| [isConstruction](SketchControlPointSpline_isConstruction.htm) | Gets and sets whether this curve is construction geometry. |
| [isControlFrameDisplayed](SketchControlPointSpline_isControlFrameDisplayed.htm) | Gets and sets if the control frame of the curve is currently displayed. Using this property is useful to be able to determine if the controlPoints and controlFrameLines properties will return useful information or not and if the addControlPoint method will succeed or not. |
| [isDeletable](SketchControlPointSpline_isDeletable.htm) | Indicates if this sketch entity can be deleted. There are cases, especially with sketch points where another entity is dependent on an entity so deleting it is not allowed. For example, you can't delete the center point of circle by itself but deleting the circle will delete the point. The same is true for the end points of a line. |
| [isFixed](SketchControlPointSpline_isFixed.htm) | Indicates if this geometry is "fixed". |
| [isFullyConstrained](SketchControlPointSpline_isFullyConstrained.htm) | Indicates if this sketch entity is fully constrained. |
| [isLinked](SketchControlPointSpline_isLinked.htm) | Indicates if this sketch entity was created by a projection, inclusion, or driven by an API script. If this returns true, then the entity is presented to the user as not editable and with a 'break link' command available. |
| [isReference](SketchControlPointSpline_isReference.htm) | Indicates if this geometry is a reference. Changing this property from true to false removes the reference. This property can not be set to true if it is already false. |
| [isValid](SketchControlPointSpline_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](SketchControlPointSpline_isVisible.htm) | When a sketch is created, geometry is sometimes automatically added to the sketch. For example a sketch point that references the origin point is always included and if a face was selected to create the sketch on, geometry from the face is also included. This automatically created geometry behaves in a special way in that it is invisible but is available for selection and it also participates in profile calculations. It's not possible to make them visible but they can be deleted and they can be used for any other standard sketch operation. |
| [length](SketchControlPointSpline_length.htm) | Returns the length of the curve in centimeters. |
| [nativeObject](SketchControlPointSpline_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](SketchControlPointSpline_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentSketch](SketchControlPointSpline_parentSketch.htm) | Returns the parent sketch. |
| [referencedEntity](SketchControlPointSpline_referencedEntity.htm) | Returns the referenced entity in the case where IsReference is true. However, this property can also return null when IsReference is true in the case where the reference is not parametric. |
| [sketchDimensions](SketchControlPointSpline_sketchDimensions.htm) | Returns the sketch dimensions that are attached to this curve. |
| [startSketchPoint](SketchControlPointSpline_startSketchPoint.htm) | The sketch point at the start of the spline. If the curve is closed the start and end sketch points will be the same. |
| [worldGeometry](SketchControlPointSpline_worldGeometry.htm) | Returns a NurbsCurve3D object that is the equivalent of this sketch curve but is in the space of the parent component rather than in sketch space. |

## Accessed From

[SketchControlPointSpline.createForAssemblyContext](SketchControlPointSpline_createForAssemblyContext.htm), [SketchControlPointSpline.nativeObject](SketchControlPointSpline_nativeObject.htm), [SketchControlPointSplines.add](SketchControlPointSplines_add.htm), [SketchControlPointSplines.item](SketchControlPointSplines_item.htm)

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |