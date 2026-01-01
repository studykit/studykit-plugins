# PerpendicularToSurfaceConstraint Object

Derived from: [GeometricConstraint](GeometricConstraint.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PerpendicularToSurfaceConstraint.h>

## Description

A sketch constraint defining that a curve is perpendicular to a face or construction plane. Line and spline curves are supported.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PerpendicularToSurfaceConstraint_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](PerpendicularToSurfaceConstraint_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](PerpendicularToSurfaceConstraint_deleteMe.htm) | Deletes this constraint. The IsDeletable property can be used to determine if this constraint can be deleted. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](PerpendicularToSurfaceConstraint_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](PerpendicularToSurfaceConstraint_attributes.htm) | Returns the collection of attributes associated with this geometric constraint. |
| [curve](PerpendicularToSurfaceConstraint_curve.htm) | Returns the SketchCurve object that is constrained. |
| [entityToken](PerpendicularToSurfaceConstraint_entityToken.htm) | Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint. |
| [isDeletable](PerpendicularToSurfaceConstraint_isDeletable.htm) | Indicates if this constraint is deletable. |
| [isValid](PerpendicularToSurfaceConstraint_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nativeObject](PerpendicularToSurfaceConstraint_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](PerpendicularToSurfaceConstraint_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentSketch](PerpendicularToSurfaceConstraint_parentSketch.htm) | Returns the parent sketch object. |
| [surface](PerpendicularToSurfaceConstraint_surface.htm) | Returns the BRepFace or ConstructionPlane the line is constrained to be perpendicular to. |

## Accessed From

[GeometricConstraints.addPerpendicularToSurface](GeometricConstraints_addPerpendicularToSurface.htm), [PerpendicularToSurfaceConstraint.createForAssemblyContext](PerpendicularToSurfaceConstraint_createForAssemblyContext.htm), [PerpendicularToSurfaceConstraint.nativeObject](PerpendicularToSurfaceConstraint_nativeObject.htm)

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |