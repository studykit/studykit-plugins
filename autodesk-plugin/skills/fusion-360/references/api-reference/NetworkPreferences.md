# NetworkPreferences Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/NetworkPreferences.h>

## Description

The NetworkPreferences object provides access to network related preferences.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](NetworkPreferences_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](NetworkPreferences_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [networkProxySetting](NetworkPreferences_networkProxySetting.htm) | Gets and sets the network proxy setting. |
| [objectType](NetworkPreferences_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [proxyHost](NetworkPreferences_proxyHost.htm) | Gets and sets the proxy host. |
| [proxyPort](NetworkPreferences_proxyPort.htm) | Gets and sets the proxy host. |

## Accessed From

[Preferences.networkPreferences](Preferences_networkPreferences.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |