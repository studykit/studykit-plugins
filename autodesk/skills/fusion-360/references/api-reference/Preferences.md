# Preferences Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/Preferences.h>

## Description

The Preferences object provides access to the various preference related objects for getting and setting the various preference values.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Preferences_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [apiPreferences](Preferences_apiPreferences.htm) | Gets the APIPreferences object, which provides access to the various preferences associated with the API. |
| [defaultUnitsPreferences](Preferences_defaultUnitsPreferences.htm) | Gets the DefaultUnitsPreferences object. |
| [generalPreferences](Preferences_generalPreferences.htm) | Gets the GeneralPreferences object. |
| [graphicsPreferences](Preferences_graphicsPreferences.htm) | Gets the GraphicsPreferences object. |
| [gridPreferences](Preferences_gridPreferences.htm) | Gets the GridPreferences object. |
| [isValid](Preferences_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [materialPreferences](Preferences_materialPreferences.htm) | Gets the MaterialPreferences object. |
| [networkPreferences](Preferences_networkPreferences.htm) | Gets the NetworkPreferences object. |
| [objectType](Preferences_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [productPreferences](Preferences_productPreferences.htm) | Gets the ProductPreferences object. |
| [productUsageData](Preferences_productUsageData.htm) | Gets the ProductUsageData object. |
| [unitAndValuePreferences](Preferences_unitAndValuePreferences.htm) | Gets the UnitAndValuePreferences object. |

## Accessed From

[Application.preferences](Application_preferences.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |