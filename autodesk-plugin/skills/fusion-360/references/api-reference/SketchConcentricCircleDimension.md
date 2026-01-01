# SketchConcentricCircleDimension Object

Derived from: [SketchDimension](SketchDimension.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConcentricCircleDimension.h>

## Description

A concentric circle dimension in a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SketchConcentricCircleDimension_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](SketchConcentricCircleDimension_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](SketchConcentricCircleDimension_deleteMe.htm) | Deletes this dimension. The IsDeletable property indicates if this dimension can be deleted. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](SketchConcentricCircleDimension_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](SketchConcentricCircleDimension_attributes.htm) | Returns the collection of attributes associated with this sketch dimension. |
| [circleOne](SketchConcentricCircleDimension_circleOne.htm) | Returns the first concentric circle or arc. |
| [circleTwo](SketchConcentricCircleDimension_circleTwo.htm) | Returns the second concentric circle or arc. |
| [entityToken](SketchConcentricCircleDimension_entityToken.htm) | Returns a token for the SketchDimension object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch dimension. |
| [isDeletable](SketchConcentricCircleDimension_isDeletable.htm) | Indicates if this dimension is deletable. |
| [isDriving](SketchConcentricCircleDimension_isDriving.htm) | Gets and sets if the dimension is Driving or is Driven. Setting this property to true for a given dimension may fail if the result would over constrain the sketch. Fusion does not allow over-constrained sketches. |
| [isValid](SketchConcentricCircleDimension_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nativeObject](SketchConcentricCircleDimension_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](SketchConcentricCircleDimension_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parameter](SketchConcentricCircleDimension_parameter.htm) | Returns the associated parameter or null if there is no associated parameter. |
| [parentSketch](SketchConcentricCircleDimension_parentSketch.htm) | Returns the parent sketch object. |
| [textPosition](SketchConcentricCircleDimension_textPosition.htm) | Gets and sets position of the dimension text. |
| [value](SketchConcentricCircleDimension_value.htm) | Gets and sets the current value of the sketch dimension.   In a parametric modeling design and the isDriving property is True, this is exactly equivalent to getting the parameter associated with the dimension and editing its value. Editing this property will result in the parameter value being changed. If isDriving is False, this acts as a read-only property and attempting to set it will fail.   In a direct modeling design the parameter property will return null and this property can be used to get and set the value of the dimension because in this case, there isn't an associated parameter.   The value is always in internal units which means that for dimensions that represent a distance, the value is in Centimeters and for dimensions representing an angle the value is in Radians. |

## Accessed From

[SketchConcentricCircleDimension.createForAssemblyContext](SketchConcentricCircleDimension_createForAssemblyContext.htm), [SketchConcentricCircleDimension.nativeObject](SketchConcentricCircleDimension_nativeObject.htm), [SketchDimensions.addConcentricCircleDimension](SketchDimensions_addConcentricCircleDimension.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |