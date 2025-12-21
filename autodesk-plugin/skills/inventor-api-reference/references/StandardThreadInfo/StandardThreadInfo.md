# StandardThreadInfo Object

Derived from: [ThreadInfo](../ThreadInfo/ThreadInfo.md) Object

## Description

The StandardThreadInfo object defines the thread information that is used by the Hole and Thread features. For tapered threads the TaperedThreadInfo object is used.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../StandardThreadInfo/StandardThreadInfo_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Class](../StandardThreadInfo/StandardThreadInfo_Class.md) | Property that returns the thread class. For example a valid class for an inch internal thread is '2B'. A valid class for a metric external thread is '6g'. |
| [CustomThreadDesignation](../StandardThreadInfo/StandardThreadInfo_CustomThreadDesignation.md) | Indicates the custom thread designation from the Custom Thread Designation column of the thread data spreadsheet. |
| [FullThreadDepth](../StandardThreadInfo/StandardThreadInfo_FullThreadDepth.md) | Gets whether this thread is the full length of the cylinder or cone. |
| [Internal](../StandardThreadInfo/StandardThreadInfo_Internal.md) | Gets and sets whether this is an internal thread or external (False). |
| [MajorDiameterMax](../StandardThreadInfo/StandardThreadInfo_MajorDiameterMax.md) | Property that gets and sets the maximum major diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [MajorDiameterMin](../StandardThreadInfo/StandardThreadInfo_MajorDiameterMin.md) | Property that gets and sets the minimum major diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [Metric](../StandardThreadInfo/StandardThreadInfo_Metric.md) | Gets and sets whether this thread is metric or not. |
| [MinorDiameterMax](../StandardThreadInfo/StandardThreadInfo_MinorDiameterMax.md) | Property that returns the maximum minor diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [MinorDiameterMin](../StandardThreadInfo/StandardThreadInfo_MinorDiameterMin.md) | Property that returns the minimum minor diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [NominalSize](../StandardThreadInfo/StandardThreadInfo_NominalSize.md) | Property that returns the description of the nominal size. Any string is valid but the following examples are typical of the strings used, '1.6', 'M4', and '9/16'. |
| [Pitch](../StandardThreadInfo/StandardThreadInfo_Pitch.md) | Property that returns the actual thread pitch. This value is used when displaying the threads in the model. This value is in millimeters if the Metric argument is True and inches if False. |
| [PitchDiameterMax](../StandardThreadInfo/StandardThreadInfo_PitchDiameterMax.md) | Property that returns the maximum pitch diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [PitchDiameterMin](../StandardThreadInfo/StandardThreadInfo_PitchDiameterMin.md) | Property that returns the minimum pitch diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [RightHanded](../StandardThreadInfo/StandardThreadInfo_RightHanded.md) | Gets and sets whether this is a right handed thread or left handed (False). |
| [TapDrillDiameter](../StandardThreadInfo/StandardThreadInfo_TapDrillDiameter.md) | Property that returns the maximum pitch diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [ThreadBasePoints](../StandardThreadInfo/StandardThreadInfo_ThreadBasePoints.md) | Property that returns an enumerator of Point objects indicating the base points for the thread. Typically, there is only one item in the collection. The exception is a hole feature based on multiple sketch points, in which case there are as many Point objects returned as there are sketch points. The point accounts for any offsets applied to the thread. The property returns a point only when the ThreadInfo object is obtained from a feature and returns Nothing in the forward create scenario. |
| [ThreadDesignation](../StandardThreadInfo/StandardThreadInfo_ThreadDesignation.md) | Property that returns a string that contains the thread designation. This is the full thread designation that is used in a drawing for the thread callout. |
| [ThreadDirection](../StandardThreadInfo/StandardThreadInfo_ThreadDirection.md) | Property that returns the direction of the thread. The property returns a vector only when the ThreadInfo object is obtained from a feature and returns Nothing in the forward create scenario. |
| [ThreadType](../StandardThreadInfo/StandardThreadInfo_ThreadType.md) | Gets and sets the thread type. |
| [ThreadTypeIdentifier](../StandardThreadInfo/StandardThreadInfo_ThreadTypeIdentifier.md) | Property that returns the string that identifies the thread type. This string is not localized and should not be changed by the user. The thread type is the name of the sheet in the Thread.xls file. |
| [Type](../StandardThreadInfo/StandardThreadInfo_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ThreadFeatures.CreateStandardThreadInfo](../ThreadFeatures/ThreadFeatures_CreateStandardThreadInfo.md)

## Derived Classes

[HoleTapInfo](../HoleTapInfo/HoleTapInfo.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Edit thread features](../../sample-programs/ThreadFeatures_CreateStandardThreadInfo_Sample.md) | The following example demonstrates how to edit an existing thread feature. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |