# HoleTapInfo Object

Derived from: [StandardThreadInfo](../StandardThreadInfo/StandardThreadInfo.md) Object

## Description

This object is really a StandardThreadInfo object with the addition of the property specifying which of the various diameter dimensions to use to model the cylindrical surface of the hole.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../HoleTapInfo/HoleTapInfo_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Class](../HoleTapInfo/HoleTapInfo_Class.md) | Property that returns the thread class. For example a valid class for an inch internal thread is '2B'. A valid class for a metric external thread is '6g'. |
| [CustomThreadDesignation](../HoleTapInfo/HoleTapInfo_CustomThreadDesignation.md) | Indicates the custom thread designation from the Custom Thread Designation column of the thread data spreadsheet. |
| [FullThreadDepth](../HoleTapInfo/HoleTapInfo_FullThreadDepth.md) | Gets whether this thread is the full length of the cylinder or cone. |
| [Internal](../HoleTapInfo/HoleTapInfo_Internal.md) | Gets and sets whether this is an internal thread or external (False). |
| [MajorDiameterMax](../HoleTapInfo/HoleTapInfo_MajorDiameterMax.md) | Property that gets and sets the maximum major diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [MajorDiameterMin](../HoleTapInfo/HoleTapInfo_MajorDiameterMin.md) | Property that gets and sets the minimum major diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [Metric](../HoleTapInfo/HoleTapInfo_Metric.md) | Gets and sets whether this thread is metric or not. |
| [MinorDiameterMax](../HoleTapInfo/HoleTapInfo_MinorDiameterMax.md) | Property that returns the maximum minor diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [MinorDiameterMin](../HoleTapInfo/HoleTapInfo_MinorDiameterMin.md) | Property that returns the minimum minor diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [NominalSize](../HoleTapInfo/HoleTapInfo_NominalSize.md) | Property that returns the description of the nominal size. Any string is valid but the following examples are typical of the strings used, '1.6', 'M4', and '9/16'. |
| [Pitch](../HoleTapInfo/HoleTapInfo_Pitch.md) | Property that returns the actual thread pitch. This value is used when displaying the threads in the model. This value is in millimeters if the Metric argument is True and inches if False. |
| [PitchDiameterMax](../HoleTapInfo/HoleTapInfo_PitchDiameterMax.md) | Property that returns the maximum pitch diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [PitchDiameterMin](../HoleTapInfo/HoleTapInfo_PitchDiameterMin.md) | Property that returns the minimum pitch diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [RightHanded](../HoleTapInfo/HoleTapInfo_RightHanded.md) | Gets and sets whether this is a right handed thread or left handed (False). |
| [TapDrillDiameter](../HoleTapInfo/HoleTapInfo_TapDrillDiameter.md) | Property that returns the maximum pitch diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [ThreadBasePoints](../HoleTapInfo/HoleTapInfo_ThreadBasePoints.md) | Property that returns an enumerator of Point objects indicating the base points for the thread. Typically, there is only one item in the collection. The exception is a hole feature based on multiple sketch points, in which case there are as many Point objects returned as there are sketch points. The point accounts for any offsets applied to the thread. The property returns a point only when the ThreadInfo object is obtained from a feature and returns Nothing in the forward create scenario. |
| [ThreadDepth](../HoleTapInfo/HoleTapInfo_ThreadDepth.md) | Property that returns the parameter that controls the depth of the thread. Even though the parameter for the thread depth is always created and accessible through this property, it is only used in the case where the FullDepth property is False. |
| [ThreadDesignation](../HoleTapInfo/HoleTapInfo_ThreadDesignation.md) | Property that returns a string that contains the thread designation. This is the full thread designation that is used in a drawing for the thread callout. |
| [ThreadDirection](../HoleTapInfo/HoleTapInfo_ThreadDirection.md) | Property that returns the direction of the thread. The property returns a vector only when the ThreadInfo object is obtained from a feature and returns Nothing in the forward create scenario. |
| [ThreadType](../HoleTapInfo/HoleTapInfo_ThreadType.md) | Gets and sets the thread type. |
| [ThreadTypeIdentifier](../HoleTapInfo/HoleTapInfo_ThreadTypeIdentifier.md) | Property that returns the string that identifies the thread type. This string is not localized and should not be changed by the user. The thread type is the name of the sheet in the Thread.xls file. |
| [Type](../HoleTapInfo/HoleTapInfo_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[HoleFeatures.CreateTapInfo](../HoleFeatures/HoleFeatures_CreateTapInfo.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole Feature - Through holes (RegularAndTapped)](../../sample-programs/HoleFeature_Sample.md) | This sample demonstrates the creation of through holes, both regular and tapped. |

## Version

Introduced in version 5
