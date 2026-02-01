# Property Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/Property.h>

## Description

The base class for the specific property types used by materials and appearances.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Property_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [id](Property_id.htm) | Returns the unique ID of this property. |
| [isReadOnly](Property_isReadOnly.htm) | Indicates if this property is read-only. If True any attempted edits will fail. |
| [isValid](Property_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](Property_name.htm) | Returns the name of this property as seen in the user interface. This name is localized and can change based on the current language |
| [objectType](Property_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](Property_parent.htm) | Returns the parent of this property.For properties associated with an appearance this will return the parent Appearance. For properties associated with a material, this will return the parent Material. For other types of properties, this will return the PropertyGroup it is in. |

## Accessed From

[ConfigurationPropertyColumn.parentProperty](ConfigurationPropertyColumn_parentProperty.htm), [Properties.item](Properties_item.htm), [Properties.itemById](Properties_itemById.htm), [Properties.itemByName](Properties_itemByName.htm), [PropertyGroup.item](PropertyGroup_item.htm), [PropertyGroup.itemById](PropertyGroup_itemById.htm), [PropertyGroup.itemByName](PropertyGroup_itemByName.htm)

## Derived Classes

[AppearanceTextureProperty](AppearanceTextureProperty.htm), [BooleanProperty](BooleanProperty.htm), [ChoiceProperty](ChoiceProperty.htm), [ColorProperty](ColorProperty.htm), [FilenameProperty](FilenameProperty.htm), [FloatProperty](FloatProperty.htm), [IntegerProperty](IntegerProperty.htm), [StringProperty](StringProperty.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Library Item API Sample](LibraryItemSample_Sample.htm) | Demonstrates how to examine library items using the API.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the existing default code. The script will search for and record all components and library items in the current project. They are displayed in a dialog when the script has finished. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |