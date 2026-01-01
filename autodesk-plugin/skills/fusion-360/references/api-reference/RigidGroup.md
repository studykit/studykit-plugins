# RigidGroup Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroup.h>

## Description

Represents a rigid group within an assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](RigidGroup_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](RigidGroup_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](RigidGroup_deleteMe.htm) | Deletes this rigid group. |
| [setOccurrences](RigidGroup_setOccurrences.htm) | Sets which occurrences are to be part of this rigid group. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](RigidGroup_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](RigidGroup_attributes.htm) | Returns the collection of attributes associated with this rigid group. |
| [entityToken](RigidGroup_entityToken.htm) | Returns a token for the RigidGroup object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same rigid group.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [isSuppressed](RigidGroup_isSuppressed.htm) | Gets and sets if this rigid group is suppressed. |
| [isValid](RigidGroup_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](RigidGroup_isVisible.htm) | Gets and sets whether the occurrences that are part of this rigid group are visible or not. |
| [name](RigidGroup_name.htm) | Gets and sets the name of the rigid group as seen in the timeline. |
| [nativeObject](RigidGroup_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](RigidGroup_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [occurrences](RigidGroup_occurrences.htm) | Returns the list of occurrences that are part of the rigid group. |
| [parentComponent](RigidGroup_parentComponent.htm) | Returns the parent component that owns this rigid group. |
| [timelineObject](RigidGroup_timelineObject.htm) | Returns the timeline object associated with this rigid group. |

## Accessed From

[Component.allRigidGroups](Component_allRigidGroups.htm), [FlatPatternComponent.allRigidGroups](FlatPatternComponent_allRigidGroups.htm), [RigidGroup.createForAssemblyContext](RigidGroup_createForAssemblyContext.htm), [RigidGroup.nativeObject](RigidGroup_nativeObject.htm), [RigidGroupList.item](RigidGroupList_item.htm), [RigidGroupList.itemByName](RigidGroupList_itemByName.htm), [RigidGroups.add](RigidGroups_add.htm), [RigidGroups.item](RigidGroups_item.htm), [RigidGroups.itemByName](RigidGroups_itemByName.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Rigid Group API Sample](RigidGroupSample_Sample.htm) | Demonstrates creating a new Rigid Group. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |