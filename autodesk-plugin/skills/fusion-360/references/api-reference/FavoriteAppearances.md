# FavoriteAppearances Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Materials/FavoriteAppearances.h>

## Description

Collection of the favorite appearances.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](FavoriteAppearances_add.htm) | Adds an existing appearance to the Favorites list |
| [classType](FavoriteAppearances_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](FavoriteAppearances_item.htm) | Returns the specified Appearance using an index into the collection. |
| [itemById](FavoriteAppearances_itemById.htm) | Returns the Appearance by it's internal unique ID. |
| [itemByName](FavoriteAppearances_itemByName.htm) | Returns the specified appearance using the name as seen in the user interface. This often isn't a reliable way of accessing a specific appearance because appearances are not required to be unique. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](FavoriteAppearances_count.htm) | The number of Appearances in the collection. |
| [isValid](FavoriteAppearances_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](FavoriteAppearances_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Application.favoriteAppearances](Application_favoriteAppearances.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |