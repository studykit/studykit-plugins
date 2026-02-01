# ThreadDataQuery Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadDataQuery.h>

## Description

This object provides methods to query the thread data contained in the XML files in ThreadData folder within the Fusion install folder. You can use the queried values to create a ThreadInfo object that is then used to create a thread feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [allClasses](ThreadDataQuery_allClasses.htm) | Returns and array/list of all the available classes for a thread type of a given thread designation. |
| [allDesignations](ThreadDataQuery_allDesignations.htm) | returns an array/list of all the available thread designations for a thread type of a given size. Valid thread types and sizes and be obtained by using the allThreadTypes and allSizes functions. |
| [allSizes](ThreadDataQuery_allSizes.htm) | Returns an array/list of all the available thread sizes for a given thread type. You can use the allThreadTypes property to get the available thread types. |
| [classType](ThreadDataQuery_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](ThreadDataQuery_create.htm) | Static method to create a new ThreadDataQuery object. The ThreadDataQuery object is a utility object that provides methods to query for the valid thread definitions defined in Fusion. This object provides similar functionality as the Thread and Hole command dialogs to find valid thread types, designations and classes which can be used to create thread and tapped hole features. |
| [recommendThreadData](ThreadDataQuery_recommendThreadData.htm) | Method that gets the recommended thread data for a given cylinder diameter. This method is only valid for straight threads and will fail for tapered threads. |
| [threadTypeCustomName](ThreadDataQuery_threadTypeCustomName.htm) | Method that returns the custom name for a given thread type. The custom name is the localized name of the thread type using the current language specified for Fusion. |
| [threadTypeUnit](ThreadDataQuery_threadTypeUnit.htm) | Method that returns the unit for a given thread type. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [allThreadTypes](ThreadDataQuery_allThreadTypes.htm) | This method returns an array of all the available thread types (families). The type names are always English. This English name should be used in the other methods that take the type as an input argument. If you need to display the type name to the user, you can use the threadTypeCustomName method To get the localized name. |
| [defaultInchThreadType](ThreadDataQuery_defaultInchThreadType.htm) | Gets the default thread type for inch threads. |
| [defaultMetricThreadType](ThreadDataQuery_defaultMetricThreadType.htm) | Gets the default thread type for metric threads. |
| [isTapered](ThreadDataQuery_isTapered.htm) | Returns if this ThreadDataQuery was created to query for standard or tapered threads. |
| [isValid](ThreadDataQuery_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ThreadDataQuery_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ThreadDataQuery.create](ThreadDataQuery_create.htm), [ThreadFeatures.threadDataQuery](ThreadFeatures_threadDataQuery.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Thread Feature API Sample](ThreadFeatureSample_Sample.htm) | Demonstrates creating a new thread feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |