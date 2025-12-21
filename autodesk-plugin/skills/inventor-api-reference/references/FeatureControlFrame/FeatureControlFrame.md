# FeatureControlFrame Object

## Description

The FeatureControlFrame object represents a feature control frame symbol on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../FeatureControlFrame/FeatureControlFrame_Delete.md) | Method that deletes the FeatureControlFrame. |
| [GetReferenceKey](../FeatureControlFrame/FeatureControlFrame_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FeatureControlFrame/FeatureControlFrame_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../FeatureControlFrame/FeatureControlFrame_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DatumIdentifier](../FeatureControlFrame/FeatureControlFrame_DatumIdentifier.md) | Gets and sets a datum identifier for the feature control frame. Setting this property fails if the associated style does not allow the specification of a datum identifier. |
| [FeatureControlFrameRows](../FeatureControlFrame/FeatureControlFrame_FeatureControlFrameRows.md) | Gets and sets the FeatureControlFrameRows object. |
| [Layer](../FeatureControlFrame/FeatureControlFrame_Layer.md) | Gets and sets the layer associated with this object. |
| [Leader](../FeatureControlFrame/FeatureControlFrame_Leader.md) | Property that returns the leader associated with the feature control frame symbol. |
| [MergeSymbolOverridden](../FeatureControlFrame/FeatureControlFrame_MergeSymbolOverridden.md) | Gets whether the OverrideMergeSymbol is set to override the MergeSymbol setting in FeatureControlFrameStyle. Set this to False will clear the override setting. |
| [Notes](../FeatureControlFrame/FeatureControlFrame_Notes.md) | Gets and sets notes for the feature control frame. The string can contain symbols specified using the StyleOverride tag. For instance, use 'm' to specify (M). |
| [OverrideMergeSymbol](../FeatureControlFrame/FeatureControlFrame_OverrideMergeSymbol.md) | Gets and sets the merge symbol override value. Set this property will set the MergeSymbolOverridden to True. |
| [Parent](../FeatureControlFrame/FeatureControlFrame_Parent.md) | Property that returns the parent Sheet object. |
| [Position](../FeatureControlFrame/FeatureControlFrame_Position.md) | Gets and sets the position of the symbol on the sheet. |
| [ProfileType](../FeatureControlFrame/FeatureControlFrame_ProfileType.md) | Gets and sets the profile type for the feature control frame. |
| [Rotation](../FeatureControlFrame/FeatureControlFrame_Rotation.md) | Gets and sets the absolute rotation angle of the symbol in radians. The value can either be positive (counter-clockwise rotation) or negative (clockwise rotation). |
| [Style](../FeatureControlFrame/FeatureControlFrame_Style.md) | Gets and sets the associated FeatureControlFrameStyle object. |
| [TopNotes](../FeatureControlFrame/FeatureControlFrame_TopNotes.md) | Gets and sets top notes for the feature control frame. The string can contain symbols specified using the StyleOverride tag. For instance, use 'm' to specify (M). |
| [Type](../FeatureControlFrame/FeatureControlFrame_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AuxiliaryFeatureIndicator.Parent](../AuxiliaryFeatureIndicator/AuxiliaryFeatureIndicator_Parent.md), [FeatureControlFrameRow.Parent](../FeatureControlFrameRow/FeatureControlFrameRow_Parent.md), [FeatureControlFrames.Add](../FeatureControlFrames/FeatureControlFrames_Add.md), [FeatureControlFrames.Item](../FeatureControlFrames/FeatureControlFrames_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding and editing a feature control frame](../../sample-programs/FeatureControlFrame_FeatureControlFrameRows_Sample.md) | These samples demonstrate editing an existing feature control frame symbol. The first sample adds a row to an existing symbol. The second sample replaces all rows of an existing symbol. |

## Version

Introduced in version 2009
