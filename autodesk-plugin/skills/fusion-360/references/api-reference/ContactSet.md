# ContactSet Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ContactSet.h>

## Description

Represents a contact set in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ContactSet_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](ContactSet_deleteMe.htm) | Deletes this contact set from the design. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isSuppressed](ContactSet_isSuppressed.htm) | Gets and sets if this contact set is currently suppressed. |
| [isValid](ContactSet_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](ContactSet_name.htm) | Gets and sets the name of the contact set. |
| [objectType](ContactSet_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [occurencesAndBodies](ContactSet_occurencesAndBodies.htm) | Gets and sets the group of Occurrence and/or BRepBody objects that are part of this contact set. |

## Accessed From

[ContactSets.add](ContactSets_add.htm), [ContactSets.item](ContactSets_item.htm), [ContactSets.itemByName](ContactSets_itemByName.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SliderJointMotion API Sample](SliderJointMotionSample_Sample.htm) | Demonstrates creating a joint with slider joint motion. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |