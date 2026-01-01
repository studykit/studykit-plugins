# CircularPatternConstraint Object

Derived from: [GeometricConstraint](GeometricConstraint.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CircularPatternConstraint.h>

## Description

A circular pattern constraint in a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CircularPatternConstraint_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](CircularPatternConstraint_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](CircularPatternConstraint_deleteMe.htm) | Deletes this constraint. The IsDeletable property can be used to determine if this constraint can be deleted. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](CircularPatternConstraint_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](CircularPatternConstraint_attributes.htm) | Returns the collection of attributes associated with this geometric constraint. |
| [centerPoint](CircularPatternConstraint_centerPoint.htm) | Gets and sets the sketch point that defines the center of the pattern. |
| [createdEntities](CircularPatternConstraint_createdEntities.htm) | Returns an array that contains all of the sketch entities that were created as a result of the pattern. This does not contain the original entities that were used as input to the pattern. The input entities can be obtained by using the entities property. |
| [entities](CircularPatternConstraint_entities.htm) | Gets and sets the entities to pattern. Sketch points and curves are valid entities to pattern. |
| [entityToken](CircularPatternConstraint_entityToken.htm) | Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint. |
| [isDeletable](CircularPatternConstraint_isDeletable.htm) | Indicates if this constraint is deletable. |
| [isSuppressed](CircularPatternConstraint_isSuppressed.htm) | Specifies which, if any, instances of the pattern are suppressed. This returns an array of Boolean values that indicates if a particular instance in the pattern is suppressed or not. A value of true will result in the associated instance being suppressed. |
| [isSymmetric](CircularPatternConstraint_isSymmetric.htm) | Gets and sets if the angle extent is in one direction or is symmetric. |
| [isValid](CircularPatternConstraint_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nativeObject](CircularPatternConstraint_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](CircularPatternConstraint_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentSketch](CircularPatternConstraint_parentSketch.htm) | Returns the parent sketch object. |
| [quantity](CircularPatternConstraint_quantity.htm) | Returns the parameter that controls the number of instances in the pattern. To change the value, use the properties on the returned ModelParameter object. |
| [totalAngle](CircularPatternConstraint_totalAngle.htm) | Returns the parameter that controls the number of instances in the pattern. A positive angle is a counter-clockwise direction and a negative angle can be used to reverse the direction. An angle of 360 degrees or 2 pi radians will create a full circular pattern. |

## Accessed From

[CircularPatternConstraint.createForAssemblyContext](CircularPatternConstraint_createForAssemblyContext.htm), [CircularPatternConstraint.nativeObject](CircularPatternConstraint_nativeObject.htm), [GeometricConstraints.addCircularPattern](GeometricConstraints_addCircularPattern.htm)

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |