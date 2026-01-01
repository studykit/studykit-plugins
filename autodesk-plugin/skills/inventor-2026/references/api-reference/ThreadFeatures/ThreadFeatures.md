# ThreadFeatures Object

## Description

The ThreadFeatures object provides access to all of the objects in a component definition and provides methods to create additional ThreadFeature objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ThreadFeatures/ThreadFeatures_Add.md) | Method that creates a new ThreadFeature. The new ThreadFeature object is returned. |
| [CreateStandardThreadInfo](../ThreadFeatures/ThreadFeatures_CreateStandardThreadInfo.md) | Method that creates a new HoleTapInfo object that can be used in creating threads for Hole features. See the Thread.xls \file that is delivered with Autodesk Inventor for examples of valid input for these arguments. Internal \Input Boolean that indicates if the thread is an internal or external thread. A value of True indicates an Internal thread. RightHanded : Input Boolean that indicates if the thread is right or left-handed thread. A value of True indicates a right-handed thread. ThreadType : Input String that specifies the sheet in the Thread.xls that this thread information should be validated within. Each sheet within the Excel document is typically used for different thread types. The string is the name of the sheet. For example "ANSI Unified Screw Threads" or "ANSI Metric M Profile" are valid for English versions of Autodesk Inventor. ThreadDesignation : Input String that contains the thread designation. This is input as the full thread designation that will be used in a drawing for the thread callout. The nominal size and pitch information are extracted from the designation. For example valid inch thread designations are '10-24 UNC' and '7/16-20 UNF'. Examples of valid metric designations are 'M16x1.5' and 'M55x1.5'. Class : Input String that defines the thread class. For \example a valid class for an inch internal thread is 2B. A valid class for a metric external thread is 6g. |
| [CreateTaperedThreadInfo](../ThreadFeatures/ThreadFeatures_CreateTaperedThreadInfo.md) | Method that creates a new TaperedThreadInfo object that can be used in creating Hole and ThreadFeature objects. See the Thread.xls file that is delivered with Autodesk Inventor for examples of valid input for these arguments. The spreadsheet columns match one for one with these arguments. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ThreadFeatures/ThreadFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../ThreadFeatures/ThreadFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../ThreadFeatures/ThreadFeatures_Item.md) | Returns the specified ThreadFeature object from the collection. This is the default property of the ThreadFeatures collection object. |
| [Type](../ThreadFeatures/ThreadFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Features.ThreadFeatures](../Features/Features_ThreadFeatures.md), [PartFeatures.ThreadFeatures](../PartFeatures/PartFeatures_ThreadFeatures.md), [SheetMetalFeatures.ThreadFeatures](../SheetMetalFeatures/SheetMetalFeatures_ThreadFeatures.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |
| [Edit thread features](../../sample-programs/ThreadFeatures_CreateStandardThreadInfo_Sample.md) | The following example demonstrates how to edit an existing thread feature. |

## Version

Introduced in version 5
