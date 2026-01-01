# CoincidentConstraint Object

Derived from: [GeometricConstraint](GeometricConstraint.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CoincidentConstraint.h>

## Description

A coincident constraint in a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CoincidentConstraint_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](CoincidentConstraint_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](CoincidentConstraint_deleteMe.htm) | Deletes this constraint. The IsDeletable property can be used to determine if this constraint can be deleted. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](CoincidentConstraint_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](CoincidentConstraint_attributes.htm) | Returns the collection of attributes associated with this geometric constraint. |
| [entity](CoincidentConstraint_entity.htm) | The sketch curve or point the point is constrained to. |
| [entityToken](CoincidentConstraint_entityToken.htm) | Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint. |
| [isDeletable](CoincidentConstraint_isDeletable.htm) | Indicates if this constraint is deletable. |
| [isValid](CoincidentConstraint_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nativeObject](CoincidentConstraint_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](CoincidentConstraint_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentSketch](CoincidentConstraint_parentSketch.htm) | Returns the parent sketch object. |
| [point](CoincidentConstraint_point.htm) | Returns the sketch point that is constrained. |

## Accessed From

[CoincidentConstraint.createForAssemblyContext](CoincidentConstraint_createForAssemblyContext.htm), [CoincidentConstraint.nativeObject](CoincidentConstraint_nativeObject.htm), [GeometricConstraints.addCoincident](GeometricConstraints_addCoincident.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |