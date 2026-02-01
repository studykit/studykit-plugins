# DraftAnalysis Object

## Description

The DraftAnalysis object represents an existing draft analysis feature in a part document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../DraftAnalysis/DraftAnalysis_Activate.md) | Method that activates the draft analysis. |
| [Copy](../DraftAnalysis/DraftAnalysis_Copy.md) | Method that creates a copy of the draft analysis. |
| [Delete](../DraftAnalysis/DraftAnalysis_Delete.md) | Method that deletes the draft analysis. |
| [GetReferenceKey](../DraftAnalysis/DraftAnalysis_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DraftAnalysis/DraftAnalysis_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DraftAnalysis/DraftAnalysis_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DisplayQuality](../DraftAnalysis/DraftAnalysis_DisplayQuality.md) | Gets/Sets the resolution or surface quality for the color gradient or color bands that represent the draft analysis results. |
| [EndAngle](../DraftAnalysis/DraftAnalysis_EndAngle.md) | Gets/Sets the end angle for the draft analysis. |
| [Faces](../DraftAnalysis/DraftAnalysis_Faces.md) | Gets/Sets the faces for the draft analysis. |
| [GradientDisplay](../DraftAnalysis/DraftAnalysis_GradientDisplay.md) | Gets/Sets whether the draft analysis results should be displayed as a color gradient. |
| [Name](../DraftAnalysis/DraftAnalysis_Name.md) | Gets and sets the name of the draft analysis. |
| [Parent](../DraftAnalysis/DraftAnalysis_Parent.md) | Property that returns the parent AnalysisManager object. |
| [PullDirection](../DraftAnalysis/DraftAnalysis_PullDirection.md) | Gets/Sets the object that specifies the direction in which the draft is applied. |
| [PullDirectionReversed](../DraftAnalysis/DraftAnalysis_PullDirectionReversed.md) | Gets/Sets whether the pull direction of the draft should be reversed. |
| [StartAngle](../DraftAnalysis/DraftAnalysis_StartAngle.md) | Gets/Sets the start angle for the draft analysis. |
| [Type](../DraftAnalysis/DraftAnalysis_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DraftAnalyses.Add](../DraftAnalyses/DraftAnalyses_Add.md), [DraftAnalyses.Item](../DraftAnalyses/DraftAnalyses_Item.md), [DraftAnalysis.Copy](../DraftAnalysis/DraftAnalysis_Copy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a Draft Analysis](../../sample-programs/DraftAnalyses_Add_Sample.md) | This sample demonstrates the creation of a draft analysis in a part. |

## Version

Introduced in version 2009
