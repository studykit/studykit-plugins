# ArrangeSelections Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ArrangeSelections.h>

## Description

Collection for all arrange selections to be passed to a CAMArrangeParameterValue object. This is a read-only container. It returns the arrange selections associated with the parent parameter value object, but does not write to it. To apply changes done to the collection and the selections it contains, CAMArrangeParameterValue.applyArrangeSelections() needs to be called.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ArrangeSelections_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [clear](ArrangeSelections_clear.htm) | Clears all entries. |
| [createNewArrangeSelection](ArrangeSelections_createNewArrangeSelection.htm) | Creates a new occurrence selection meant for arrange operations and adds it to the end of the collection. |
| [item](ArrangeSelections_item.htm) | Function that returns the specified arrange selection object using an index into the collection. |
| [remove](ArrangeSelections_remove.htm) | Function that removes the specified arrange selection object using an index in the collection. |
| [removeByObject](ArrangeSelections_removeByObject.htm) | Function that removes the specified arrange selection object from the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ArrangeSelections_count.htm) | The number of items in the collection. |
| [isValid](ArrangeSelections_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ArrangeSelections_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAMArrangeParameterValue.getArrangeSelections](CAMArrangeParameterValue_getArrangeSelections.htm)

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |