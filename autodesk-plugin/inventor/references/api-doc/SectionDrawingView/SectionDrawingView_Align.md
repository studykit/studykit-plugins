# SectionDrawingView.Align Method

Parent Object: [SectionDrawingView](../SectionDrawingView/SectionDrawingView.md)

## Description

Method that aligns this view with the input drawing view. The method returns a failure if the view is already aligned. Use the Aligned property to check for this condition and to break existing alignment.

## Syntax

SectionDrawingView.**Align**( ***DrawingView*** As [DrawingView](../DrawingView/DrawingView.md), ***AlignmentType*** As [DrawingViewAlignmentEnum](../DrawingViewAlignmentEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DrawingView | [DrawingView](../DrawingView/DrawingView.md) | Input DrawingView object that specifies the view with which to align this view. |
| AlignmentType | [DrawingViewAlignmentEnum](../DrawingViewAlignmentEnum.md) | Input DrawingViewAlignmentEnum that specifies the alignment type. Valid values are kHorizontalViewAlignment, kVerticalViewAlignment and kInPositionViewAlignment. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |