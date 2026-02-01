# BalloonTip.OnClick Event

Parent Object: [BalloonTip](../BalloonTip/BalloonTip.md)

## Description

Event that fires when the BalloonTip object is clicked on a hyperlink.

## Syntax

BalloonTip.**OnClick**( ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. Currently the following name-value pair is supported.   * Name = "HyperlinkIndex", Value = Long. The Index of the hyper link that was clicked. |

## Version

Introduced in version 2012
