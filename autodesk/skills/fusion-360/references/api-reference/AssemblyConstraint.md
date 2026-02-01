# AssemblyConstraint Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AssemblyConstraint.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Represents an assembly constraint.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](AssemblyConstraint_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](AssemblyConstraint_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](AssemblyConstraint_deleteMe.htm) | Deletes this assembly constraint. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](AssemblyConstraint_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](AssemblyConstraint_attributes.htm) | Returns the collection of attributes associated with this assembly constraint. |
| [entityToken](AssemblyConstraint_entityToken.htm) | Returns a token for the assembly constraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same assembly constraint. |
| [errorOrWarningMessage](AssemblyConstraint_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [geometricRelationships](AssemblyConstraint_geometricRelationships.htm) | Returns the set of geometric relationships used for this assembly constraint. |
| [healthState](AssemblyConstraint_healthState.htm) | Returns the current health state of the assembly constraint. |
| [isLightBulbOn](AssemblyConstraint_isLightBulbOn.htm) | Gets and sets if the light bulb of this assembly constraint, as displayed in the browser, is on or off. An assembly constraint will only be visible if the light bulb is switched on. However, the light bulb can be on and the assembly constraint still invisible if a higher level occurrence in the assembly context is not visible because its light bulb is off or the light bulb of the parent Joints folder is off. |
| [isSuppressed](AssemblyConstraint_isSuppressed.htm) | Gets and sets if this assembly constraint is suppressed. If suppressed, all of the assembly constraints within the will be suppressed. |
| [isValid](AssemblyConstraint_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](AssemblyConstraint_isVisible.htm) | Gets whether the assembly constraint is visible. To change the visibility see the isLightBulbOn property. This property is affected by the assembly context. |
| [name](AssemblyConstraint_name.htm) | Gets and sets the name of the assembly constraint. This is the name seen in the browser and timeline. |
| [nativeObject](AssemblyConstraint_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](AssemblyConstraint_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentComponent](AssemblyConstraint_parentComponent.htm) | Returns the parent component that owns this assembly constraint. |
| [timelineObject](AssemblyConstraint_timelineObject.htm) | Returns the timeline object associated with this assembly constraint. |

## Accessed From

[AssemblyConstraint.createForAssemblyContext](AssemblyConstraint_createForAssemblyContext.htm), [AssemblyConstraint.nativeObject](AssemblyConstraint_nativeObject.htm), [AssemblyConstraints.add](AssemblyConstraints_add.htm), [AssemblyConstraints.item](AssemblyConstraints_item.htm), [AssemblyConstraints.itemByName](AssemblyConstraints_itemByName.htm), [Component.allAssemblyConstraints](Component_allAssemblyConstraints.htm), [FlatPatternComponent.allAssemblyConstraints](FlatPatternComponent_allAssemblyConstraints.htm)

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |