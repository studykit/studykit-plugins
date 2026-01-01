# ConfigurationReplaceDesign Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationReplaceDesign.h>

## Description

This object represents an individual ConfigurationReplaceDesign object that has been defined for a ConfigurationReplaceDesignColumn. Multiple ConfigurationReplaceDesign objects can be defined for a column and then one of those ConfigurationReplaceDesign objects is specified in each cell of the column.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationReplaceDesign_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](ConfigurationReplaceDesign_deleteMe.htm) | Deletes this ConfigurationReplaceDesign. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [dataFile](ConfigurationReplaceDesign_dataFile.htm) | Gets the Design object associated with this ConfigurationReplaceDesign object. This must be a DataFile object that represents a standard design, not a configured design. |
| [isValid](ConfigurationReplaceDesign_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](ConfigurationReplaceDesign_name.htm) | Gets the name of the ConfigurationReplaceDesign object. |
| [objectType](ConfigurationReplaceDesign_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ConfigurationInsertStandardDesignCell.replaceDesign](ConfigurationInsertStandardDesignCell_replaceDesign.htm), [ConfigurationReplaceDesigns.add](ConfigurationReplaceDesigns_add.htm), [ConfigurationReplaceDesigns.item](ConfigurationReplaceDesigns_item.htm), [ConfigurationReplaceDesigns.itemByName](ConfigurationReplaceDesigns_itemByName.htm)

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |