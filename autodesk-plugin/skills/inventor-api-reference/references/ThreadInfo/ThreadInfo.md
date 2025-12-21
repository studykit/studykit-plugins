# ThreadInfo Object

## Description

This is a common base object from which the rest of the concrete objects that hold thread information are derived. It contains the generally applicable properties of threads.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ThreadInfo/ThreadInfo_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CustomThreadDesignation](../ThreadInfo/ThreadInfo_CustomThreadDesignation.md) | Indicates the custom thread designation from the Custom Thread Designation column of the thread data spreadsheet. |
| [FullThreadDepth](../ThreadInfo/ThreadInfo_FullThreadDepth.md) | Gets whether this thread is the full length of the cylinder or cone. |
| [Internal](../ThreadInfo/ThreadInfo_Internal.md) | Gets and sets whether this is an internal thread or external (False). |
| [Metric](../ThreadInfo/ThreadInfo_Metric.md) | Gets and sets whether this thread is metric or not. |
| [RightHanded](../ThreadInfo/ThreadInfo_RightHanded.md) | Gets and sets whether this is a right handed thread or left handed (False). |
| [ThreadBasePoints](../ThreadInfo/ThreadInfo_ThreadBasePoints.md) | Property that returns an enumerator of Point objects indicating the base points for the thread. Typically, there is only one item in the collection. The exception is a hole feature based on multiple sketch points, in which case there are as many Point objects returned as there are sketch points. The point accounts for any offsets applied to the thread. The property returns a point only when the ThreadInfo object is obtained from a feature and returns Nothing in the forward create scenario. |
| [ThreadDesignation](../ThreadInfo/ThreadInfo_ThreadDesignation.md) | Property that returns a string that contains the thread designation. This is the full thread designation that is used in a drawing for the thread callout. |
| [ThreadDirection](../ThreadInfo/ThreadInfo_ThreadDirection.md) | Property that returns the direction of the thread. The property returns a vector only when the ThreadInfo object is obtained from a feature and returns Nothing in the forward create scenario. |
| [ThreadType](../ThreadInfo/ThreadInfo_ThreadType.md) | Gets and sets the thread type. |
| [ThreadTypeIdentifier](../ThreadInfo/ThreadInfo_ThreadTypeIdentifier.md) | Property that returns the string that identifies the thread type. This string is not localized and should not be changed by the user. The thread type is the name of the sheet in the Thread.xls file. |
| [Type](../ThreadInfo/ThreadInfo_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ThreadFeature.ThreadInfo](../ThreadFeature/ThreadFeature_ThreadInfo.md), [ThreadFeatureProxy.ThreadInfo](../ThreadFeatureProxy/ThreadFeatureProxy_ThreadInfo.md), [ThreadTableQuery.CreateThreadInfo](../ThreadTableQuery/ThreadTableQuery_CreateThreadInfo.md)

## Derived Classes

[StandardThreadInfo](../StandardThreadInfo/StandardThreadInfo.md), [TaperedThreadInfo](../TaperedThreadInfo/TaperedThreadInfo.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |