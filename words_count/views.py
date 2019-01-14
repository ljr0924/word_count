from django.shortcuts import render


def home(request):
    return render(request, 'word_counts.html')


def words_count(request):
    text = request.GET.get('text', 0)
    length = len(text)

    word_num = {}
    for word in text:
        if word not in word_num.keys():
            word_num[word] = 1
        else:
            word_num[word] += 1
    word_num = sorted(word_num.items(), key=lambda i: i[1], reverse=True)

    context = {}
    context['length'] = length
    context['text'] = text
    context['word_num'] = word_num
    context['max_count'] = word_num[0][0]
    print(length)
    return  render(request, 'count.html', context)