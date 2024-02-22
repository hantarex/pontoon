import pytest

from pontoon.tags.utils import Tags


@pytest.fixture
def chart_0():
    return {
        "total_strings": 0,
        "approved_strings": 0,
        "pretranslated_strings": 0,
        "strings_with_errors": 0,
        "strings_with_warnings": 0,
        "unreviewed_strings": 0,
        "approved_share": 0,
        "pretranslated_share": 0,
        "errors_share": 0,
        "warnings_share": 0,
        "unreviewed_share": 0,
        "completion_percent": 0,
    }


@pytest.mark.django_db
def test_tags_get_no_project():
    tags = Tags().get()
    assert len(tags) == 0


@pytest.mark.django_db
def test_tags_get(
    chart_0,
    project_a,
    tag_a,
    translation_a,
):
    tags = Tags(project=project_a).get()
    tag = tags[0]

    assert tag.name == tag_a.name
    assert tag.slug == tag_a.slug
    assert tag.priority == tag_a.priority
    assert tag.latest_activity == translation_a.latest_activity

    chart = chart_0
    chart["total_strings"] = 1
    chart["unreviewed_strings"] = 1
    chart["unreviewed_share"] = 100.0
    assert tag.chart == chart


@pytest.mark.django_db
def test_tags_get_tag_locales(
    chart_0,
    project_a,
    project_locale_a,
    tag_a,
):
    tags = Tags(project=project_a, slug=tag_a.slug)
    tag = tags.get_tag_locales()

    assert tag.name == tag_a.name
    assert tag.priority == tag_a.priority
    assert tag.locales.count() == project_a.locales.all().count()
    assert tag.locales.first() == project_a.locales.all().first()

    with pytest.raises(AttributeError):
        tag.latest_activity

    chart = chart_0
    chart["total_strings"] = 1
    assert tag.chart == chart

    locale = tag.locales.first()
    assert locale.latest_activity is None
    assert locale.chart == chart
