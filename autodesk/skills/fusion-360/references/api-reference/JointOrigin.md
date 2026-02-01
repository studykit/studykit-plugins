# JointOrigin Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigin.h>

## Description

Represents an existing joint origin in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](JointOrigin_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](JointOrigin_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](JointOrigin_deleteMe.htm) | Deletes this joint origin. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [angle](JointOrigin_angle.htm) | Gets the parameter that controls the angle. The value can be changed using the functionality of the returned ModelParameter object. |
| [assemblyContext](JointOrigin_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](JointOrigin_attributes.htm) | Returns the collection of attributes associated with this joint origin. |
| [entityToken](JointOrigin_entityToken.htm) | Returns a token for the JointOrigin object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same joint origin. |
| [geometry](JointOrigin_geometry.htm) | Gets and sets the joint geometry for this joint origin input. This defines the location of the joint origin.   To set this property, you need to position the timeline marker to immediately before this joint. This can be accomplished using the following code: joint.timelineObject.rollTo(True) |
| [isFlipped](JointOrigin_isFlipped.htm) | Gets and sets if the joint origin direction is flipped or not.   To set this property, you need to position the timeline marker to immediately before this joint. This can be accomplished using the following code: joint.timelineObject.rollTo(True) |
| [isLightBulbOn](JointOrigin_isLightBulbOn.htm) | Gets and sets if the light bulb of this jointOrigin as displayed in the browser is on or off. A joint origin will only be visible if the light bulb is switched on. However, the light bulb can be on and the joint origin still invisible if a higher level occurrence in the assembly context is not visible because its light bulb is off or the joint origins folder light bulb is off. |
| [isValid](JointOrigin_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](JointOrigin_name.htm) | Gets and sets the name of this joint origin. This is the name seen by the user in the timeline. |
| [nativeObject](JointOrigin_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](JointOrigin_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [offsetX](JointOrigin_offsetX.htm) | Gets the parameter that controls the X offset direction. The value can be changed using the functionality of the returned ModelParameter object. |
| [offsetY](JointOrigin_offsetY.htm) | Gets the parameter that controls the Y offset direction. The value can be changed using the functionality of the returned ModelParameter object. |
| [offsetZ](JointOrigin_offsetZ.htm) | Gets the parameter that controls the Z offset direction. The value can be changed using the functionality of the returned ModelParameter object. |
| [parentComponent](JointOrigin_parentComponent.htm) | Returns the parent component that owns this joint origin. |
| [primaryAxisVector](JointOrigin_primaryAxisVector.htm) | Returns the direction of the primary axis that's been calculated for this joint origin. This is conceptually the Z axis as shown by the triad representing the joint origin. |
| [secondaryAxisVector](JointOrigin_secondaryAxisVector.htm) | Returns the direction of the secondary axis that's been calculated for this joint origin. This is conceptually the X axis as shown by the triad representing the joint origin. |
| [thirdAxisVector](JointOrigin_thirdAxisVector.htm) | Returns the direction of the third axis that's been calculated for this joint origin. This is conceptually the Y axis as shown by the triad representing the joint origin. |
| [timelineObject](JointOrigin_timelineObject.htm) | Returns the timeline object associated with this joint origin. |
| [transform](JointOrigin_transform.htm) | Returns the position and orientation of the joint geometry associated with this joint origin. This is returned as a 3D matrix which provides the origin and the X, Y, and Z axis vectors of the coordinate system.   This property is especially useful in cases where the JointGeometry cannot be obtained. This can happen when the model has been modified in a way where the geometry used to create the joint is no longer available. |
| [xAxisEntity](JointOrigin_xAxisEntity.htm) | Gets and sets the entity that defines the X axis direction. This defaults to null meaning the X axis is inferred from the input geometry.   To set this property, you need to position the timeline marker to immediately before this joint. This can be accomplished using the following code: joint.timelineObject.rollTo(True) |
| [zAxisEntity](JointOrigin_zAxisEntity.htm) | Gets and sets the entity that defines the Z axis direction. This defaults to null meaning the Z axis is inferred from the input geometry.   To set this property, you need to position the timeline marker to immediately before this joint. This can be accomplished using the following code: joint.timelineObject.rollTo(True) |

## Accessed From

[Component.allJointOrigins](Component_allJointOrigins.htm), [FlatPatternComponent.allJointOrigins](FlatPatternComponent_allJointOrigins.htm), [JointOrigin.createForAssemblyContext](JointOrigin_createForAssemblyContext.htm), [JointOrigin.nativeObject](JointOrigin_nativeObject.htm), [JointOriginList.item](JointOriginList_item.htm), [JointOriginList.itemByName](JointOriginList_itemByName.htm), [JointOrigins.add](JointOrigins_add.htm), [JointOrigins.item](JointOrigins_item.htm), [JointOrigins.itemByName](JointOrigins_itemByName.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Joint Origin Between Two Faces Sample](JointOrigin2Planes_Sample.htm) | Demonstrates creating a new Joint Origin between two planes. |
| [Joint Origin Sample](JointOriginSample_Sample.htm) | Demonstrates creating a new Joint Origin. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |