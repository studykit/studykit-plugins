# ProductUsageData Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/ProductUsageData.h>

## Description

Provides access to the product usage data settings.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ProductUsageData_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isGoogleAnalyticsTrackingEnabled](ProductUsageData_isGoogleAnalyticsTrackingEnabled.htm) | Gets and sets if Google Analytics tracking is enabled. |
| [isLearningPanelContextEnabled](ProductUsageData_isLearningPanelContextEnabled.htm) | Gets and sets if data can be collected to enable the Learning Panel to show information based on the current context. |
| [isTrackingToImproveCommunicationEnabled](ProductUsageData_isTrackingToImproveCommunicationEnabled.htm) | Gets and sets if data can be collected to improve communications. This is the preferences setting titled "Customize our messaging". |
| [isTrackingToImproveSoftwareEnabled](ProductUsageData_isTrackingToImproveSoftwareEnabled.htm) | Gets and sets if data can be collected to help improve the products and services that Autodesk provides. This is the preference setting titled "Help develop our products and services". |
| [isValid](ProductUsageData_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ProductUsageData_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Preferences.productUsageData](Preferences_productUsageData.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |