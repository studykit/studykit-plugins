# AssemblyConstraints Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AssemblyConstraints.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

The collection of assembly constraints in this component. This provides access to all existing assembly constraints and supports the ability to create new assembly constraints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](AssemblyConstraints_add.htm) | Creates a new assembly constraint. |
| [classType](AssemblyConstraints_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](AssemblyConstraints_createInput.htm) | Creates an assembly constraint input to define an assembly constraint. Use functionality on the returned AssemblyConstraintInput to define the input needed to create an assembly constraint. |
| [item](AssemblyConstraints_item.htm) | Function that returns the specified assembly constraint using an index into the collection. |
| [itemByName](AssemblyConstraints_itemByName.htm) | Function that returns the specified assembly constraint object using a name. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](AssemblyConstraints_count.htm) | Returns the number of assembly constraint objects in the collection. |
| [isValid](AssemblyConstraints_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](AssemblyConstraints_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Component.assemblyConstraints](Component_assemblyConstraints.htm), [FlatPatternComponent.assemblyConstraints](FlatPatternComponent_assemblyConstraints.htm)

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |