# SketchEllipticalArc Object

Derived from: [SketchCurve](SketchCurve.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipticalArc.h>

## Description

An elliptical arc in a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [breakCurve](SketchEllipticalArc_breakCurve.htm) | Breaks a curve into two or three pieces by finding intersections of this curve with all other curves in the sketch and splitting this curve at the nearest intersections to a specified point on the curve. |
| [classType](SketchEllipticalArc_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](SketchEllipticalArc_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](SketchEllipticalArc_deleteMe.htm) | Deletes the entity from the sketch. |
| [extend](SketchEllipticalArc_extend.htm) | Extend a curve by specifying a point that determines the end of the curve to extend |
| [intersections](SketchEllipticalArc_intersections.htm) | Get the curves that intersect this curve along with the intersection points (Point3D) |
| [split](SketchEllipticalArc_split.htm) | Split a curve at a position specified along the curve |
| [trim](SketchEllipticalArc_trim.htm) | Trim a curve by specifying a point that determines the segment of the curve to trim away |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](SketchEllipticalArc_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](SketchEllipticalArc_attributes.htm) | Returns the collection of attributes associated with this face. |
| [boundingBox](SketchEllipticalArc_boundingBox.htm) | Returns the bounding box of the entity in sketch space. |
| [centerSketchPoint](SketchEllipticalArc_centerSketchPoint.htm) | Gets the sketch point that defines the center of the elliptical arc. You can reposition the elliptical arc by moving the sketch point, assuming any existing constraints allow the desired change. |
| [endSketchPoint](SketchEllipticalArc_endSketchPoint.htm) | Gets the sketch point that defines the end of the elliptical arc. You can reposition the sketch point, assuming any existing constraints allow the desired change. |
| [entityToken](SketchEllipticalArc_entityToken.htm) | Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity. |
| [geometricConstraints](SketchEllipticalArc_geometricConstraints.htm) | Returns the sketch constraints that are attached to this curve. |
| [geometry](SketchEllipticalArc_geometry.htm) | Returns the transient geometry of the elliptical arc which provides geometric information about the elliptical arc. The returned geometry is always in sketch space. |
| [is2D](SketchEllipticalArc_is2D.htm) | Indicates if this curve lies entirely on the sketch x-y plane. |
| [isConstruction](SketchEllipticalArc_isConstruction.htm) | Gets and sets whether this curve is construction geometry. |
| [isDeletable](SketchEllipticalArc_isDeletable.htm) | Indicates if this sketch entity can be deleted. There are cases, especially with sketch points where another entity is dependent on an entity so deleting it is not allowed. For example, you can't delete the center point of circle by itself but deleting the circle will delete the point. The same is true for the end points of a line. |
| [isFixed](SketchEllipticalArc_isFixed.htm) | Indicates if this geometry is "fixed". |
| [isFullyConstrained](SketchEllipticalArc_isFullyConstrained.htm) | Indicates if this sketch entity is fully constrained. |
| [isLinked](SketchEllipticalArc_isLinked.htm) | Indicates if this sketch entity was created by a projection, inclusion, or driven by an API script. If this returns true, then the entity is presented to the user as not editable and with a 'break link' command available. |
| [isReference](SketchEllipticalArc_isReference.htm) | Indicates if this geometry is a reference. Changing this property from true to false removes the reference. This property can not be set to true if it is already false. |
| [isValid](SketchEllipticalArc_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](SketchEllipticalArc_isVisible.htm) | When a sketch is created, geometry is sometimes automatically added to the sketch. For example a sketch point that references the origin point is always included and if a face was selected to create the sketch on, geometry from the face is also included. This automatically created geometry behaves in a special way in that it is invisible but is available for selection and it also participates in profile calculations. It's not possible to make them visible but they can be deleted and they can be used for any other standard sketch operation. |
| [length](SketchEllipticalArc_length.htm) | Returns the length of the curve in centimeters. |
| [majorAxis](SketchEllipticalArc_majorAxis.htm) | Gets and sets the major axis direction of the elliptical arc. Changing the axis is limited by any constraints that might exist on the elliptical arc. Setting the axis can fail in cases where the direction is fully defined through constraints. |
| [majorAxisRadius](SketchEllipticalArc_majorAxisRadius.htm) | Gets and sets the major axis radius of the elliptical arc. Changing the radius is limited by any constraints that might exist on the elliptical arc. Setting the radius can fail in cases where the radius is fully defined through constraints. |
| [minorAxisRadius](SketchEllipticalArc_minorAxisRadius.htm) | Gets and sets the minor axis radius of the elliptical arc. Changing the radius is limited by any constraints that might exist on the elliptical arc. Setting the radius can fail in cases where the radius is fully defined through constraints. |
| [nativeObject](SketchEllipticalArc_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](SketchEllipticalArc_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentSketch](SketchEllipticalArc_parentSketch.htm) | Returns the parent sketch. |
| [referencedEntity](SketchEllipticalArc_referencedEntity.htm) | Returns the referenced entity in the case where IsReference is true. However, this property can also return null when IsReference is true in the case where the reference is not parametric. |
| [sketchDimensions](SketchEllipticalArc_sketchDimensions.htm) | Returns the sketch dimensions that are attached to this curve. |
| [startSketchPoint](SketchEllipticalArc_startSketchPoint.htm) | Gets the sketch point that defines the start of the elliptical arc. You can reposition the sketch point, assuming any existing constraints allow the desired change. |
| [worldGeometry](SketchEllipticalArc_worldGeometry.htm) | Returns an EllipticalArc3D object which provides geometric information in world space. The returned geometry takes into account the assembly context and the position of the sketch in it's parent component, which means the geometry will be returned in the root component space. |

## Accessed From

[SketchEllipticalArc.createForAssemblyContext](SketchEllipticalArc_createForAssemblyContext.htm), [SketchEllipticalArc.nativeObject](SketchEllipticalArc_nativeObject.htm), [SketchEllipticalArcs.addByAngle](SketchEllipticalArcs_addByAngle.htm), [SketchEllipticalArcs.addByEndPoints](SketchEllipticalArcs_addByEndPoints.htm), [SketchEllipticalArcs.item](SketchEllipticalArcs_item.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |