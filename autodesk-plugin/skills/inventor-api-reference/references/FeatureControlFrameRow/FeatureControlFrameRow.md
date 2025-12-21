# FeatureControlFrameRow Object

## Description

The FeatureControlFrameRow object represents a row within a feature control frame symbol.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../FeatureControlFrameRow/FeatureControlFrameRow_Delete.md) | The row of the feature control frame. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FeatureControlFrameRow/FeatureControlFrameRow_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AuxiliaryFeatureIndicators](../FeatureControlFrameRow/FeatureControlFrameRow_AuxiliaryFeatureIndicators.md) | Gets the AuxiliaryFeatureIndicators collection object. |
| [DatumOne](../FeatureControlFrameRow/FeatureControlFrameRow_DatumOne.md) | Gets and sets the first datum that affects the tolerance. Returns a null string if the datum is not specified. The string can contain symbols specified using the StyleOverride tag. E.g. use 'm' to specify (M). |
| [DatumThree](../FeatureControlFrameRow/FeatureControlFrameRow_DatumThree.md) | Gets and sets the third datum that affects the tolerance. Returns a null string if the datum is not specified. The string can contain symbols specified using the StyleOverride tag. E.g. use 'm'to specify (M). |
| [DatumTwo](../FeatureControlFrameRow/FeatureControlFrameRow_DatumTwo.md) | Gets and sets the second datum that affects the tolerance. Returns a null string if the datum is not specified. The string can contain symbols specified using the StyleOverride tag. E.g. use 'm' to specify (M). |
| [GeometricCharacteristic](../FeatureControlFrameRow/FeatureControlFrameRow_GeometricCharacteristic.md) | Gets and sets the geometric characteristic symbol for the row. |
| [InlineNote](../FeatureControlFrameRow/FeatureControlFrameRow_InlineNote.md) | Gets and sets the inline note. This is applicable only when the FeatureControlFrameStyle.EnableInlineNotes is set to True when the style is applied to this FeatureControlFrame object. |
| [LowerTolerance](../FeatureControlFrameRow/FeatureControlFrameRow_LowerTolerance.md) | Gets and sets the lower tolerance associated with this geometric characteristic. Applies to ANSI standard only. The string can contain symbols specified using the StyleOverride tag. E.g. use 'm' to specify (M). |
| [Parent](../FeatureControlFrameRow/FeatureControlFrameRow_Parent.md) | Property that returns the parent FeatureControlFrame object. |
| [Tolerance](../FeatureControlFrameRow/FeatureControlFrameRow_Tolerance.md) | Gets and sets the tolerance associated with this geometric characteristic. The string can contain symbols specified using the StyleOverride tag. E.g. use 'm' to specify (M). |
| [Type](../FeatureControlFrameRow/FeatureControlFrameRow_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FeatureControlFrameRows.Add](../FeatureControlFrameRows/FeatureControlFrameRows_Add.md), [FeatureControlFrameRows.Item](../FeatureControlFrameRows/FeatureControlFrameRows_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding and editing a feature control frame](../../sample-programs/FeatureControlFrame_FeatureControlFrameRows_Sample.md) | These samples demonstrate editing an existing feature control frame symbol. The first sample adds a row to an existing symbol. The second sample replaces all rows of an existing symbol. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |