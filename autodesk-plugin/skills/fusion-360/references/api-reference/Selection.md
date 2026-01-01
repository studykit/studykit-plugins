# Selection Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Selection.h>

## Description

Provides access to a selection of an entity in the user interface.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Selection_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [entity](Selection_entity.htm) | Gets the selected entity. |
| [isValid](Selection_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Selection_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [point](Selection_point.htm) | Gets the selection point on the object. |

## Accessed From

[ActiveSelectionEventArgs.currentSelection](ActiveSelectionEventArgs_currentSelection.htm), [SelectionCommandInput.selection](SelectionCommandInput_selection.htm), [SelectionEventArgs.selection](SelectionEventArgs_selection.htm), [Selections.asArray](Selections_asArray.htm), [Selections.item](Selections_item.htm), [UserInterface.selectEntity](UserInterface_selectEntity.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |